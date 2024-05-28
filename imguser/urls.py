# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_image, name='upload_image'),
    path('success/', views.success, name='success'),
    path('profile/', views.display_profile, name='display_profile'),
]
