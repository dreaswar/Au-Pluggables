################################################################################
# PROJECT      : AuShadha
# Description  : dynamic_aushadha_models Models
# Author       : Dr. Easwar T R
# Date         : 16-09-2013
# Licence      : GNU GPL V3. Please see AuShadha/LICENSE.txt
################################################################################


import datetime
import yaml
import os

from django.db import models
from django.contrib.auth.models import User
from django.db.models.loading import cache  
from django.db import connection

from south.db import db #This should be removed once migrations are better supported in Django1.7

from AuShadha.apps.aushadha_base_models.models import AuShadhaBaseModel,AuShadhaBaseModelForm
from AuShadha.settings import APP_ROOT_URL
from AuShadha.apps.ui.ui import ui as UI

DEFAULT_FORM_EXCLUDES=('',)


# Put all Models and ModelForms below this

APP_PATH = os.path.dirname(__file__)
DEFAULT_YAML = 'DynamicAuShadhaModel.yaml'
DEFAULT_YAML_PATH = os.path.join(APP_PATH, DEFAULT_YAML)

#model_yaml = open(os.path.join(APP_PATH, DEFAULT_YAML))
#model_yaml_dict = yaml.load(model_yaml)
#model_yaml.close()




def check_if_table_is_present(model_class_list, create_if_it_passes = True):

    """ Checks if the db table is present for a model class and if create option is True creates the DB table """

    for model_class in model_class_list:
        table = model_class._meta.db_table
        tables = connection.introspection.table_names()
        if table in tables:
           s = "Duplicate Table with name: %s Exists. Please rename your class" %(table)
           raise Exception(s) 

    if create_if_it_passes:
      for model_class in model_class_list:
          _create_table_and_fields(model_class)


def _create_table_and_fields(model_class):

    """ creates a table and fields """

    fields = [(f.name, f) for f in model_class._meta.local_fields]
    table_name = model_class._meta.db_table
    db.create_table(table_name, fields)
    db.execute_deferred_sql()

def _create_or_alter_table_and_fields(model_class):

    """ This has to create or alter table based on what values exist. This should also handle migrations """

    return





class YAMLLoadingModel(object):

  
  """
    This will load the YAML file, make it attributes of self.
    This is then passed on to the type constructor down the line.

    self.returned_fields : Returned on call to the instance
    
  """


  def __init__(self, model_to_load, yaml_path =DEFAULT_YAML_PATH):
     
     self.yaml_dict = None
     self.field_dict = {}
     self.model_to_load = model_to_load
     if yaml_path == DEFAULT_YAML_PATH:
      self.yaml_path = yaml_path
     else:
       self.yaml_path = os.path.join(APP_PATH,yaml_path)

     self.clear_the_model_cache()  #This clears the model cache is a similar modelClass exists. relevent only for runtime changes ? 
     self.set_up_model()           #Sets up the model
     self.load_model()
     self.field_dict['__module__'] =  self.yaml_dict['__module__']


  def _set_up_fields(self, model_to_load):  

     """ Sets up the model class fields including the __module__ field  """ 

     self.returned_fields = {
                        '__doc__': model_to_load['__doc__'],
                        '__module__': self.yaml_dict['__module__'] 
                       }

     for field in model_to_load['fields']:
        f_name  = field['name']
        val = getattr(models, field['field_type'])(*field['args'], **field['kwargs'])
        self.returned_fields[ field['name'] ] =  val


  def clear_the_model_cache(self):

    """ To deal the Django's model class caching behaviour """

    try:
      del cache.app_models['dynamic_aushadha_models'][self.model_to_load]
    except KeyError:
      pass    


  def set_up_model(self):

     """ Loads the YAML file and parses out the model_classes key """

     model_yaml = open( self.yaml_path  )
     self.yaml_dict = yaml.load( model_yaml )
     model_yaml.close()
     self.model_classes = self.yaml_dict['model_classes']
     setattr(self, '__module__', self.yaml_dict['__module__'])
     self.field_dict[ '__module__' ] = self.yaml_dict['__module__']


  def load_model(self):

     """ Loads the Model from the model_classes parsed from YAML and sets up the Django model fields """

     for model in self.model_classes:
       if model['class'] == self.model_to_load:
         self._set_up_fields(model)


  def __call__(self):

    """ 
       Calling the YAMLLoadingModel with return the self.returned_fields
       This dict is used to pass to the TableMaker class for making tables

    """
        
    print("Calling YAMLLoadingModel")
    print(self.returned_fields)
    return self.returned_fields




class TableMaker(object):



  def __init__(self,
               class_name,
               model_class, 
               super_class = (AuShadhaBaseModel,), 
               yaml_path = DEFAULT_YAML_PATH):

      self.super_class = super_class
      self.yaml_path = yaml_path
      self.class_name = class_name
      self.model_class = model_class

      self.created_class = type(self.class_name,
                                self.super_class,
                                YAMLLoadingModel(self.model_class,self.yaml_path)()
                               )

      self.clear_the_model_cache()
      self.check_if_table_is_present()


  def to_model(self):

      return self.created_class


  def clear_the_model_cache(self):

      try:
          del cache.app_models['dynamic_aushadha_models'][self.created_class]
      except KeyError:
          pass    


  def check_if_table_is_present(self, create_if_it_passes = True):

      table = self.created_class._meta.db_table
      tables = connection.introspection.table_names()

      if table in tables:
           s = "Duplicate Table with name: %s Exists. Please rename your class" %(table)
           raise Exception(s) 

      if create_if_it_passes:
          _create_table_and_fields(self.created_class)



  def _create_table_and_fields():

      """ creates a table and fields """

      fields = [(f.name, f) for f in self.created_class._meta.local_fields]
      table_name = self.created_class._meta.db_table
      db.create_table(table_name, fields)
      db.execute_deferred_sql()



  def _create_or_alter_table_and_fields(model_class):

      """ This has to create or alter table based on what values exist. This should also handle migrations """

      return

