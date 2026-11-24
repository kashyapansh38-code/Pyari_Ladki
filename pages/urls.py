from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('fun/', views.fun, name='fun'),
    path('motivation/', views.motivation, name='motivation'),
    path('message/', views.message, name='message'),
]