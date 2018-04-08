from django.test import TestCase
from title.models import Task,Sub
# Create your tests here.
class TaskTestCase(TestCase):
    def setUp(self):
        Task.objects.create(titles="First Task")
        
