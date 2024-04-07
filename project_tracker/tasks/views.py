from .models import Project, Task
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from django.views.generic import DetailView

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'tasks/index.html')
class ProjectsListView(ListView):
    model = Project
    template_name = 'tasks/projects_list.html'
class ProjectDetailView(DetailView):
    model = Project
    pk_url_kwarg = 'project_id'
    template_name = 'tasks/project_detail.html'
class TaskDetailView(DetailView):
    model = Task
    pk_url_kwarg = 'task_id'
    template_name = 'tasks/task_detail.html'