from django.contrib import admin
from .models import Phone

class PhoneAdmin(admin.ModelAdmin):
    list_display = ['patient_detail', 'country_code', 'area_code', 'phone']

admin.site.register(Phone, PhoneAdmin)

