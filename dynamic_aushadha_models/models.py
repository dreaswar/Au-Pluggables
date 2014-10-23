################################################################################
# PROJECT      : AuShadha
# Description  : dynamic_aushadha_models Models
# Author       : Dr. Easwar T R
# Date         : 16-09-2013
# Licence      : GNU GPL V3. Please see AuShadha/LICENSE.txt
################################################################################


from django.db import models

from AuShadha.apps.aushadha_base_models.models import AuShadhaBaseModel,AuShadhaBaseModelForm

from yaml_loader import YAMLLoadingModel, TableMaker, check_if_table_is_present

DEFAULT_FORM_EXCLUDES=('',)


# Put all Models and ModelForms below this
# Model Definition Starts here. 


DynamicAuShadhaModel = TableMaker(yaml_path = "DynamicAuShadhaModel.yaml",
                                  class_name = "DynamicAuShadhaModel", 
                                  model_class="DynamicAuShadhaModel").to_model()

DetailedNeuroSystemExam = TableMaker(yaml_path = "DetailedNeuroSystemExam.yaml",
                                     class_name = "DetailedNeuroSystemExam", 
                                     model_class="DetailedNeuroSystemExam").to_model()

SpeechAndLanguageFunctions = TableMaker(yaml_path = "DetailedNeuroSystemExam.yaml",
                                     class_name = "SpeechAndLanguageFunctions", 
                                     model_class="SpeechAndLanguageFunctions").to_model()

HigherMentalFunctions = TableMaker(yaml_path = "DetailedNeuroSystemExam.yaml",
                                   class_name = "HigherMentalFunctions", 
                                   model_class="HigherMentalFunctions").to_model()



################################# This works as well ##################################################################
# The first model is a test model
#  it does nothing. 

# Others are actual model classes intented for AuShadha
# The code below prepares the classes 
# SQL table creation occurs after introspection down

#DynamicAuShadhaModel= type('DynamicAuShadhaModel',
#                            (AuShadhaBaseModel,),
#                            YAMLLoadingModel('DynamicAuShadhaModel')()
#                          )

#DetailedNeuroSystemExam= type('DetailedNeuroSystemExam',
#                            (AuShadhaBaseModel,),
#                            YAMLLoadingModel('DetailedNeuroSystemExam','DetailedNeuroSystemExam.yaml')()
#                          )

#SpeechAndLanguageFunctions= type('SpeechAndLanguageFunctions',
#                            (AuShadhaBaseModel,),
#                            YAMLLoadingModel('SpeechAndLanguageFunctions','DetailedNeuroSystemExam.yaml')()
#                          )

#HigherMentalFunctions= type('HigherMentalFunctions',
#                            (AuShadhaBaseModel,),
#                            YAMLLoadingModel('HigherMentalFunctions','DetailedNeuroSystemExam.yaml')()
#                          )


# Actually check the model exists as table and raise exception if there is
# We are not creating runtime migrations here
# So if there is a table by the same name Exception is thrown and process aborted

#model_list = [DynamicAuShadhaModel, DetailedNeuroSystemExam, SpeechAndLanguageFunctions, HigherMentalFunctions]
#check_if_table_is_present(model_list)
