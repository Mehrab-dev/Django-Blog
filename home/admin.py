from django.contrib import admin
from home.models import Contact

class ContactAdmin(admin.ModelAdmin) :
    date_hierarchy = 'created_date'
    list_display = ['name','email','subject','created_date']
    search_fields = ['email']

admin.site.register(Contact,ContactAdmin)