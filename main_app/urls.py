# We create this urls.py in main_app to seperate the app's urls and project's urls
from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('int:cat_id/', views.show, name='show'),

  # We set up a route to post a new Cat, post_url to listen for a post request
  path('post_url/', views.post_cat, name='post_cat')
]

