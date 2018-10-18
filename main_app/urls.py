# We create this urls.py in main_app to seperate the app's urls and project's urls
from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
]

