from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='index'),
   path('resources/', views.resources, name='resources'),
   path('meetings/', views.meetings, name='meetings'),
   path('meetingdetail/<int:id>', views.meetingdetail, name='detail'),
   path('newResource/', views.newResource, name='newresource'),
   path('newMeeting/', views.newMeeting, name='newmeeting'),
]