"""
URL configuration for greetings project.

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
from myapp.views import HelloWorldView
from myapp.views import GoodMorningView
from myapp.views import GoodEveningView,SelfIntroView,VehicleDetailsView,MobileDetailsView,LaptopDetailsView,WatchView,HeadphoneDetailsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("hello/",HelloWorldView.as_view()),
    path("morning/",GoodMorningView.as_view()),
    path("evening/",GoodEveningView.as_view()),
    path("intro/",SelfIntroView.as_view()),
    path('vehicle/',VehicleDetailsView.as_view()),
    path('mobile/',MobileDetailsView.as_view()),
    path('laptop/',LaptopDetailsView.as_view()),
    path('watch/',WatchView.as_view()),
    path('headphone/',HeadphoneDetailsView.as_view()),
]
