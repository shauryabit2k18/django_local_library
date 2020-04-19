from django.urls import path
from . import views


app_name = 'my_portfolio'

urlpatterns = [
    path('/' , views.index_main , name="index"),
    path('gallery/' , views.gallery, name="gallery"),
    path('contact/' , views.contact, name="contact"),
    path('about/' , views.about , name="about"),
    path('certi/' , views.certi , name="certi"),
]