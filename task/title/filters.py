from title.models import Task
import django_filters

class TaskFilter(django_filters.FilterSet):

    class Meta:
        model = Task
        fields = ['titles',]
