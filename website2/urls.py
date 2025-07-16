from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='aboutus'),
    path('contact',views.contact,name='contact'),
    path('gallery',views.gallery,name='gallery'),
    path('gallery_video',views.gallery_video,name='gallery_video'),
    path('addmission',views.addmission,name='addmission1'),
    path('fee',views.fee,name='fee'),
    path('download/', views.download_pdf, name='download_pdf'),
]