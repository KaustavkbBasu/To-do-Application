from django.conf.urls import url
from title import views

urlpatterns = [
    url(r'^$',views.AboutView.as_view(),name='about'),
    url(r'^due/$', views.overdue_task, name='due'),
    url(r'^next/$', views.next_week_task, name='next'),
    url(r'^this/$', views.this_week_task, name='this'),
    url(r'^today/$', views.today_task, name='today'),
    url(r'^search/$', views.search_task, name='search'),
    url(r'^task/new/$', views.CreateTaskView.as_view(), name='task_new'),
    url(r'^task/$',views.TaskListView.as_view(),name='task_list'),
    url(r'^task/(?P<pk>\d+)$', views.TaskDetailView.as_view(), name='task_detail'),
    url(r'^task/(?P<pk>\d+)/sub/$', views.add_sub_to_task, name='add_sub_to_task'),
    ]
