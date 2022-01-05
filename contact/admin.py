from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'content', 'created_on')
    search_fields = ['full_name', 'content']
  
admin.site.register(Contact, ContactAdmin)
