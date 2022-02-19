from django.test import TestCase
from django.contrib.auth.models import User
from .models import Meeting, MeetingMinutes, Resource, Event
import datetime
from .forms import MeetingForm, ResourceForm
from django.urls import reverse_lazy, reverse

# Create your tests here.
class MeetingTest(TestCase):
    def setUp(self):
        self.title=Meeting(meetingtitle='Retrospective')

    def test_typestring(self):
        self.assertEqual(str(self.title), 'Retrospective')

    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')

class MeetingMinutesTest(TestCase):
    def setUp(self):
        self.mins=MeetingMinutes(minutes='test meeting minutes')

    def test_typestring(self):
        self.assertEqual(str(self.mins), 'test meeting minutes')

    def test_tablename(self):
        self.assertEqual(str(MeetingMinutes._meta.db_table), 'meetingminutes')

class ResourceTest(TestCase):
    def setUp(self):
        self.name=Resource(resourcename='resource1')

    def test_typestring(self):
        self.assertEqual(str(self.name), 'resource1')

    def test_tablename(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')

class EventTest(TestCase):
    def setUp(self):
        self.title=Event(eventtitle='Eventorama')

    def test_typestring(self):
        self.assertEqual(str(self.title), 'Eventorama')

    def test_tablename(self):
        self.assertEqual(str(Event._meta.db_table), 'event')

class New_Meeting_Authentication_Test(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username='testUser1', password='P@ssw0rd!')
        self.meeting=Meeting.objects.create(meetingtitle='Planning', meetingdate='2022-02-28', location='Seattle', agenda='test agenda')

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newmeeting'))
        self.assertRedirects(response, '/accounts/login/?next=/club/newmeeting/')
