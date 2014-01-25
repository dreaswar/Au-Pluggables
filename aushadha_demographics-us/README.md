Introduction  
------------  
This the US version of the stock demographics app in AuShadha project.  
This Application is intended to replace the stock Demographics application in AuShadha and is intended to  
provide an interface for collection and storage of Demographics Data of Patients as per the US data collection methods  

This application is part of the Au-Pluggables project intended to develop pluggable, user / locale specific module 
for AuShadha Open Source EMR  


Installation  
------------  

1) Copy the folder 'aushadha_demographics-us' into AuShadha src/AuShadha directory  

2) Add  

   'aushadha_demographics-us/demographics'  
   'aushadha_demographics-us/contact'  
   'aushadha_demographics-us/phone'  
   'aushadha_demographics-us/email_and_fax'  
   'aushadha_demographics-us/guardian'  
   'aushadha_demographics-us/insurance'  

   into INSTALLED_APPS in settings.py in AuShadha  


3) Add templates folders into template directories in settings.py  
     
   'aushadha_demographics-us/demographics/templates/'  
   'aushadha_demographics-us/contact/templates/'  
   'aushadha_demographics-us/phone/templates/'  
   'aushadha_demographics-us/email_and_fax/templates/'  
   'aushadha_demographics-us/guardian/templates/'  
   'aushadha_demographics-us/insurance/templates/'  


3) Add media folders into media directories in settings.py  
     
   'aushadha_demographics-us/demographics/media/'  
   'aushadha_demographics-us/contact/media/'  
   'aushadha_demographics-us/phone/media/'  
   'aushadha_demographics-us/email_and_fax/media/'  
   'aushadha_demographics-us/guardian/media/'  
   'aushadha_demographics-us/insurance/media/'  

4) Add the include('aushadha_demographics-us/demographics.urls') into AuShadha urls.py  

5) Update configure.yaml file with the classes and roles for registration  

6) Remove the stock Demographics application from settings.py and its references in templates, media  

7) Remove the stock Demographics application in urls.py and configure.yaml  

8) Run python/manage.py syncdb and runserver to see application in action !   


