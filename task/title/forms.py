from django import forms
from title.models import Task, Sub

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('titles','due_date','status',)

class SubForm(forms.ModelForm):
    class Meta:
        model = Sub
        fields = ('titles',)
