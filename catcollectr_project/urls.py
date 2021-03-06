"""catcollectr_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import include, path
from django.contrib import admin


# imports the views.py from main_app
# from main_app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # First argument is the relative path for the URL, second is the specific path to the view function we want to associate with our route. 'index/' is for debugging and proof of concepts. Use '' root route instead
    # path('', views.index)

    path('', include('main_app.urls'))
]
