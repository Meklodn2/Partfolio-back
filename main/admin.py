from django.contrib import admin
from .models import Contact
# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','email', 'date_contacted']
    search_fields = ['name','email','messages']
    list_filter = ['date_contacted']
    date_hierarchy= 'date_contacted'
    ordering = ['date_contacted']