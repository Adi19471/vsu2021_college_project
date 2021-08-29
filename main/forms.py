from django import forms
from .models import *

# movie add form
class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('name', 'director', 'cast', 'description', 'release_date', 'image')

        


        labels = {"name":"Enter Your College Name",
        'director':"Enter Your College-Direct Name",
        'cast':'Year Of Eastablish Date',
        'description':'Enter Your College Description/Openion',
        'release_date':'Enter Your Joining Date',
        'image':"Uplode Your College Photo",
        
        }
          
        
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ("comment", "rating")
        


# contact forma page

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'



# image gallery form

class ImagesForms(forms.ModelForm):
    class Meta:
        model = Image
        fields=['img']
        labels = {'img':''}