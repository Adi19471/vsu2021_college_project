from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = "main"

urlpatterns = [
    path('',views.main,name='main'),
    path('home/', views.home,name="home"),
    path('about/',views.about,name="abt"),

    path('details/<int:id>/', views.detail, name="detail"),
    path('addcollege/', views.add_movies, name="add_movies"),
    path('editcollege/<int:id>/', views.edit_movies, name="edit_movies"),
    path('deletecollege/<int:id>/', views.delete_movies, name="delete_movie"),
    path('addreview/<int:id>/', views.add_review, name="add_review"),
    path('editreview/<int:movie_id>/<int:review_id>/', views.edit_review, name="edit_review"),
    path('deletereview/<int:movie_id>/<int:review_id>/', views.delete_review, name="delete_review"),


    path('contact/',views.contact,name="contact"),
    path('gallery/',views.gallery,name="gallery"),
    
    path('email/',views.Email_view,name="email"),
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

