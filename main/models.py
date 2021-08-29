from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import related
# Create your models here.
class Movie(models.Model):
    # fields for the movie table
    name = models.CharField(max_length=300)
    director = models.CharField(max_length=300)
    cast = models.CharField(max_length=800)
    description = models.TextField( max_length=5000)
    release_date = models.DateField()
    averageRating = models.FloatField(default=0)

    image = models.URLField(default=None, null=True)
    
    # image = models.ImageField(upload_to='images/')


    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "COLLEGE"

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=5000)
    rating = models.FloatField(default=0)

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name_plural = "COLLEGE_REVIEW"


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    # mobile = models.IntegerField()
    comment = models.TextField(max_length=100)
    
    def __str__(self):
        return self.first_name
    
    class Meta:
        verbose_name_plural = 'ENQUIRY DATA'



# gallery

class Image(models.Model):
   
    img = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = "IMAGES"