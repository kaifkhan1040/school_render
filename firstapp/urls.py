from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='hello'),
    path('form_submit', views.form_submit, name='form_submit'),
]