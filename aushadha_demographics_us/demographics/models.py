################################################################################
# Description  : Patient Models for managing Patient Demographics 
# Author       : Dr. Easwar T R
# Date         : 16-09-2013
# Licence      : GNU GPL V3. Please see AuShadha/LICENSE.txt
################################################################################

from django.db import models
from django.contrib.auth.models import User

from AuShadha.settings import APP_ROOT_URL
from AuShadha.utilities.urls import UrlGenerator, generic_url_maker
from AuShadha.apps.ui.ui import ui as UI
from AuShadha.apps.aushadha_base_models.models import AuShadhaBaseModel, AuShadhaBaseModelForm

#from patient.models import PatientDetail
PatientDetail = UI.get_module("PatientRegistration")

from dijit_fields_constants import DEMOGRAPHICS_FORM_CONSTANTS
DEFAULT_FORM_EXCLUDES = ('patient_detail',)

MARITAL_STATUS = ( ('Married', 'married'), 
                  ('Single', 'single'),
                  ('Divorced','divorced'), 
                  ('Separated', 'separated'),
                  ('Partner', 'partner') ,
                )

BARRIERS_TO_COMMUNICATION = ( ('Language', 'language'), 
                              ('Hearing', 'hearing'), 
                              ('Seeing', 'seeing'), 
                            )



class Demographics(AuShadhaBaseModel):

    """
      Maintains Demographics data for the patient.
      This has been adapted from the excellent work by GNU Health project.
    """

    def __init__(self, *args, **kwargs):
      super(Demographics,self).__init__(*args, **kwargs)
      self.__model_label__ = "demographics"
      self._parent_model = 'patient_detail'

    date_of_birth = models.DateField(auto_now_add=False,
                                     null=True,
                                     blank=True,
                                     help_text = "MM/DD/YYYY"
                                    )
    medical_record_number = models.CharField(max_length = 100, unique = True) 
    social_security_number = models.CharField(max_length = 100, unique = True, help_text  = "Format: xxx-xx-xxxx") 

    marital_status	 = models.CharField(max_length = 100, choices = MARITAL_STATUS)
    race = models.CharField(max_length=200)
    languages_known = models.TextField(max_length=300)
    barriers_to_communication        = models.CharField(max_length = 100, choices = BARRIERS_TO_COMMUNICATION)

    occupation = models.CharField(max_length = 100)
    employer_name = models.CharField(max_length = 100)
    employer_address = models.TextField(max_length = 1000)
    employer_city   = models.CharField(max_length = 100)
    employer_state = models.CharField(max_length = 100, help_text = "Abbreviation")
    employer_country = models.CharField(max_length = 30)
    employer_zip_code = models.CharField(max_length = 100)
    employer_phone  = models.CharField(max_length = 100, help_text = "(xxx)-xxx-xxxx")

    patient_detail = models.ForeignKey(PatientDetail,
                                       null=True,
                                       blank=True,
                                       unique=True
                                       )

    def __unicode__(self):
        return " Demographics for - %s" % (self.patient_detail)

    def _field_list(self):
        self.field_list = []
        print self._meta.fields
        for field in self._meta.fields:
            self.field_list.append(field)
        return self.field_list

    def formatted_obj_data(self):
        field_list = self._field_list()
        str_obj = "<ul>"
        for obj in field_list:
            _str = "<li>" + obj + "<li>"
            str_obj += _str
        str_obj += "</ul>"
        return str_obj



################################################################################


class US_StateRegistry(AuShadhaBaseModel):

  """
   Registry for US States, Abbreviations and Zip-Codes
  """
  state_name = models.CharField(max_length = 100, unique = True)
  abbreviation = models.CharField(max_length = 3, unique = True)

  class Meta:
    unique_together = ('state_name', 'abbreviation')
    verbose_name = "US States"
    verbose_name_plural = "US States"



class US_CityRegistry(AuShadhaBaseModel):

  """
   Registry for US Cities
  """
  city_name = models.CharField(max_length = 100, unique = True)
  state = models.ForeignKey('US_StateRegistry')

  class Meta:
    unique_together = ('state', 'city_name')
    verbose_name = "US Cities"
    verbose_name_plural = "US Cities"



class US_ZipCodeRegistry(AuShadhaBaseModel):

  """
   US Zip Code Registry
  """

  zip_codes    = models.CharField(max_length = 100, unique  = True )
  state = models.ForeignKey('US_StateRegistry')

  class Meta:
    unique_together = ('zip_codes', 'state')
    verbose_name = "US Zip Code Registry"
    verbose_name_plural = "US Zip Code Registry"


class LanguageRegistry(AuShadhaBaseModel):
  """
   Languages Registry
  
  """
  language_name = models.CharField(max_length = 100, unique = True)


class RaceRegistry(AuShadhaBaseModel):
  """
   Race Registry 
  """
  race_name = models.CharField(max_length = 100, unique = True)




############################# Model Forms ######################################


class DemographicsForm(AuShadhaBaseModelForm):

    """
        ModelForm for Demographics Data Recording
    """

    __form_name__ = "Demographics Form"

    dijit_fields = DEMOGRAPHICS_FORM_CONSTANTS

    class Meta:
        model = Demographics
        exclude = DEFAULT_FORM_EXCLUDES