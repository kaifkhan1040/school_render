from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='aboutus'),
    path('contact',views.contact,name='contact'),
    path('gallery',views.gallery,name='gallery'),
    path('addmission',views.addmission,name='addmission1'),
]