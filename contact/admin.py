from django.contrib import admin
from .models import Contact

class PostAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'second_name', 'email', 'content','created_on')
    search_fields = ['title', 'content']
  
admin.site.register(Contact, PostAdmin)
