from django.urls import path
from .views import index, get_data


urlpatterns = [
    path('index/', index),
    path('data/', get_data),
]
