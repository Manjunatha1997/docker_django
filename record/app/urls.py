from django.urls import path
from app.views import *
urlpatterns = [
    path('video/',video),
    path('run/',run),
    path('run1/',run1),
]

