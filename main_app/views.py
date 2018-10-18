# A view is a function that takes in a web request and returns a web response.

# Create your views here.

# from django.http import HttpResponse

# def index(request):
	# return HttpResponse('<h1>Hello World! /ᐠ｡‸｡ᐟ\ﾉ</h1>')


from django.shortcuts import render
from .models import Cat

# In url.py this is views.index OR localhost:8000/index in browser
def index(request):
	cats = Cat.objects.all()
	return render(request, 'index.html', {'cats': cats})


# class Cat:
#   def __init__(self, name, breed, description, age):
#     self.name = name
#     self.breed = breed
#     self.description = description
#     self.age = age


cats = [
  Cat('Lolo', 'tabby', 'foul little demon', 3),
  Cat('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
  Cat('Raven', 'black tripod', '3 legged cat', 4)
]

