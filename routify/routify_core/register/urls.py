from django.urls import path
from . import views
from django.urls import path
from .views import user_form_view

urlpatterns = [
    path('register/', views.register, name='register'),
    path('user_form/', user_form_view, name='user_form_view'),
    # Other URL patterns...
]
