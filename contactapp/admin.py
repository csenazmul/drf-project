from django.contrib import admin
from .models import Contact
# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number', 'address']
    search_fields = ['name', 'email', 'phone_number']
    list_filter = ['name', 'email', 'phone_number', 'address']
    list_per_page = 10
# Compare this snippet from contactapp/views.py:
# from django.shortcuts import render   
# from rest_framework import viewsets
# from .models import Contact   
# from .serializers import ContactSerializer
#       
