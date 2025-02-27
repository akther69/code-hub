"""
URL configuration for Employee project.

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
    path("employees/all/",views.EmployeeListView.as_view(),name="emp-list"),
    path("employees/add/",views.EmployeeCreateView.as_view(),name="emp-add"),
    path("employees/<int:pk>/",views.EmployeeDetailView.as_view(),name="emp-info"),
    path("employees/<int:pk>/remove/",views.EmployeeDeleteView.as_view(),name="emp-delete"),
    path("employees/<int:pk>/change/",views.EmployeeUpdateView.as_view(),name="emp-update"),
    path("works/add/",views.WorkCreateView.as_view(),name="work-add"),
    path("works/all/",views.WorkListView.as_view(),name="work-list"),
    path("works/<int:pk>/change/",views.WorkUpdateView.as_view(),name="work-edit"),
    path("works/<int:pk>/remove/",views.WorkDeleteView.as_view(),name="work-remove"),

]
