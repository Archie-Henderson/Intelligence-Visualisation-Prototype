from django.urls import path
from data_processing import views

app_name = 'data_processing'

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload, name='upload'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
]