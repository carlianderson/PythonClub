from django.shortcuts import render
from .models import Meeting, MeetingMinutes, Resource, Event, User

# Create your views here.
def index(request):
    return render(request, 'club/index.html')

def users(request):
    user_list=User.objects.all()
    return render(request, 'club/users.html', {'user_list':user_list})