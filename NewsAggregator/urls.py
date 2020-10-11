from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path
from news import views

urlpatterns = [
    path('', views.Home, name = "home"),
    path('football', views.Cricket, name = "cricket"),
    path('cricket', views.Football, name = "football"),

    path('admin/', admin.site.urls),
]
