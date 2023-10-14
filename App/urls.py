from django.contrib import admin
from django.urls import path
from App import views
app_name = "App"
urlpatterns = [
    path('features/', views.features,name='features'),
    path('', views.about,name='about'),
]