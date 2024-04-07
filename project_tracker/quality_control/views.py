from django.http import HttpResponse
from django.urls import reverse
from .models import BugReport, FeatureRequest
from django.views.generic import DetailView

def index(request):
    bug_list_url = reverse('quality_control:bug_list')
    feature_list_url = reverse('quality_control:feature_list')
    return HttpResponse(f"<h1>Система контроля качества</h1><a href='{bug_list_url}'>Отчеты об ошибках</a><br/><a href='{feature_list_url}'>Запросы на улучшение</a>")

def bug_list(request):
    bugs = BugReport.objects.all()
    bugs_html = '<h1>Cписок отчетов об ошибках</h1><ul>'
    for bug in bugs:
        bugs_html += f'<li><a href="{bug.id}/">{bug.title}</a></li>'
    bugs_html += "</ul>"
    return HttpResponse(bugs_html)

def feature_list(request):
    features = FeatureRequest.objects.all()
    features_html = '<h1>Список запросов на улучшение</h1><ul>'
    for feature in features:
        features_html += f'<li><a href="{feature.id}/">{feature.title}</a></li>'
    features_html += "</ul>"
    return HttpResponse(features_html)

class bug_detail(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        bug = self.object
        response_html = f'<h1>{bug.title}</h1><p>description: {bug.description}</p><p>status: {bug.status}</p><p>priority: {bug.priority}</p><p>project: {bug.project}</p><p>task: {bug.task}</p>'
        response_html += '</ul>'
        
        return HttpResponse(response_html)

class feature_detail(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        feature = self.object
        response_html = f'<h1>{feature.title}</h1><p>description: {feature.description}</p><p>status: {feature.status}</p><p>priority: {feature.priority}</p><p>project: {feature.project}</p><p>task: {feature.task}</p>'
        response_html += '</ul>'
        
        return HttpResponse(response_html)