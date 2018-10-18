from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# In url.py this is views.index OR localhost:8000/index in browser
def index(request):
	return HttpResponse('<h1>Hello World! /ᐠ｡‸｡ᐟ\ﾉ</h1>')