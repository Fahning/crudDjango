from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from books.api import viewsets as bookviewsets

route = routers.DefaultRouter()
route.register(r'books', bookviewsets.BooksViewSet, basename='Books')

urlpatterns = [
    path('', include(route.urls))
]
