from django.contrib import admin
from django.db.models import fields
from .models import *

# Register your models here.

admin.site.register(Review)

# contact page create
admin.site.register(Contact)



@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    
    list_display = ['name','director','description','averageRating']
    
    list_filter = ("name", "description", "averageRating",)


# images savedin external page Html

admin.site.register(Image)


# email data base saved =email


admin.site.register(EmailData)