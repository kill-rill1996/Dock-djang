from .views import index_page

from django.urls import path, include

urlpatterns = [
    path('', index_page),
]
