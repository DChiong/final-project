from django.urls import path
from .import views

urlpatterns = [
    path('', views.index),
    path('predict', views.predict_view, name='predict'),
    path('dashboard', views.dashboard_view, name='dashboard'),
    path('home', views.home_view, name='home'),
    path('registration', views.registration_view, name='registration'),
   
 
]