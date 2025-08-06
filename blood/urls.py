from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('view_stock/', views.view_blood_stock, name='view_stock'),
    path('request_blood/', views.request_blood, name='request_blood'),
    path('register_donor/', views.register_donor, name='register_donor'),
    path( 'home', views.home, name='home'),


]
