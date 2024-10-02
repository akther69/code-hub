"""
URL configuration for FilmWorld project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from Myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("films/all/",views.FilmListView.as_view(),name="film-list"),
    path("films/add/",views.FilmCreateView.as_view(),name="film-add"),
    path("films/<int:pk>/",views.FilmDetailView.as_view(),name="film-info"),
    path("films/<int:pk>/remove/",views.FilmDeleteView.as_view(),name="film-delete"),
    path("films/<int:pk>/change/",views.FilmUpdateView.as_view(),name="film-update"),


]
