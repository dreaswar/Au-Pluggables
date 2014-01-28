from django.contrib import admin
from .models import Contact



class ContactAdmin(admin.ModelAdmin):
    list_display = ['patient_detail', 'address',
                    'city', 'state', 'country', 'zip_code']


admin.site.register(Contact, ContactAdmin)
