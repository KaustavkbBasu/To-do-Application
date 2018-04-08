from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
import datetime

# Create your models here.
class Task(models.Model):
    STATUS_CHOISE = (('pending','Pending'),('completed','Completed'),)
    titles = models.CharField(max_length=200)
    due_date = models.DateTimeField(default=timezone.now() + timezone.timedelta(60))
    create_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=200,choices=STATUS_CHOISE,default='pending')


    def __str__(self):
        return self.titles

    def get_absolute_url(self):
        return reverse("task_detail",kwargs={'pk':self.pk})


class Sub(models.Model):
    task = models.ForeignKey('title.Task',related_name="ts")
    titles = models.CharField(max_length=200,default='DEFAULT VALUE')
    # due_date = models.DateTimeField()

    def __str__(self):
        return self.titles

    def get_absolute_url(self):
        return reverse("task_list")
