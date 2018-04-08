from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from django.utils import timezone
from title.models import Task,Sub
from title.forms import TaskForm,SubForm
from django.template import loader, Context
from django.db.models import F
import operator
import datetime
from django.db.models import Q
from title.filters import TaskFilter
# Create your views here.
class AboutView(TemplateView):
    template_name = 'about.html'

class CreateTaskView(CreateView):

    redirect_field_name = 'title/title_detail.html'

    form_class = TaskForm

    model = Task

class TaskListView(ListView):
    template_name = 'title/task_list.html'
    context_object_name = 'task_list'
    model = Task

    def get_queryset(self):
        return Task.objects.filter().order_by('due_date')

class TaskDetailView(DetailView):
    model = Task

def add_sub_to_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = SubForm(request.POST)
        if form.is_valid():
            subt = form.save(commit=False)
            subt.task = task
            subt.save()
            return redirect('task_detail', pk=task.pk)
    else:
        form = SubForm()
    return render(request, 'title/sub_form.html', {'form': form})


# def search(request):
#     query = request.GET['q']
#     t = loader.get_template('title/search.html')
#     my_dict = { 'query': query,}
#     # c = Context({ 'query': query,})
#     return HttpResponse(t.render(context=my_dict))

def search_task(request):
    task_list = Task.objects.all()
    task_filter = TaskFilter(request.GET, queryset=task_list)
    return render(request, 'title/search.html', {'filter': task_filter})

def today_task(request):
    task_today = Task.objects.filter(due_date=datetime.date.today())
    return render(request, 'title/filter.html', {'today': task_today})

def this_week_task(request):
    date = datetime.date.today()
    start_week = date - datetime.timedelta(date.weekday())
    end_week = start_week + datetime.timedelta(7)
    task_this_week = Task.objects.filter(due_date__range=[start_week, end_week])
    return render(request, 'title/filter.html', {'this': task_this_week})

def next_week_task(request):
    date = datetime.date.today()
    start_week = date - datetime.timedelta(date.weekday())
    next_start_week = start_week + datetime.timedelta(7)
    # next_start_week = end_week + datetime.timedelta(1)
    next_end_week = next_start_week + datetime.timedelta(7)
    task_next_week = Task.objects.filter(due_date__range=[next_start_week, next_end_week])
    return render(request, 'title/filter.html', {'next': task_next_week})

def overdue_task(request):
    overdue = Task.objects.filter(due_date__lte = F('create_date') + datetime.timedelta(60))
    return render(request, 'title/filter.html', {'overdue': overdue})

def auto_delete(request):
    end_date = create_date + datetime.timedelta(90)
    old_task = Task.objects.filter(create_date__range=[create_date, end_date])
