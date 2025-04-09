from django.contrib import admin
from django.urls import path
from hello.views import hello_world
from hello.views import testMesage

urlpatterns = [
    path("",testMesage),
]
