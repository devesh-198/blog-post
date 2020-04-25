"""define url patterns for user"""

from django.urls import path, include
from . import views

app_name = 'user'
urlpatterns = [
    # Include a default auth urs.
    path('', include('django.contrib.auth.urls')),
    # Registration page.
    path('register/', views.register, name='register'),
]
