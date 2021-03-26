from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from rest_framework import routers
from books.api import viewsets as bookviewsets

route = routers.DefaultRouter()
route.register(r'books', bookviewsets.BooksViewSet, basename='Books')

urlpatterns = [
    path('', include(route.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
