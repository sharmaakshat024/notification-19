from django.contrib import admin
from django.urls import path, include
from LoginPage import views
urlpatterns = [
    path('', views.LoginPage, name = 'LoginPage'),
    path('RegistrationPage', views.RegistrationPage, name = 'RegistrationPage'),
    path('SelfTest', views.SelfTest, name = 'SelfTest'),
    path('Home', views.Home, name = 'Home'),
    path('DataAnalysis', views.DataAnalysis, name = 'DataAnalysis'),
]
