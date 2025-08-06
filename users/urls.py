from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('view_stock/', views.view_stock, name='view_stock'),
    path('request_blood/', views.request_blood, name='request_blood'),

]
