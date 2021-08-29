from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Review)

# contact page create
admin.site.register(Contact)



@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    
    list_display = ['name','director','description','averageRating']
    
    list_filter = ("name", "description", "averageRating",)

admin.site.register(Image)