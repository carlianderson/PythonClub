from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='index'),
   path('club/', views.users, name='users')
]
