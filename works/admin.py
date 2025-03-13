from django.contrib import admin
from .models import Work
# Register your models here.
@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_posted']
    search_fields = ['title', 'content']
    list_filter = ['date_posted']
    date_hierarchy = 'date_posted'
    ordering = ['date_posted']