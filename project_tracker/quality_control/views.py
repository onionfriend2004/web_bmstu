from .models import BugReport, FeatureRequest
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from .forms import BugReportForm, FeatureRequestForm
from django.urls import reverse_lazy

def index(request):
    return render(request, 'quality_control/index.html')

#FBV---------------------------------------------------------
def bug_list(request):
    bugs = BugReport.objects.all()
    return render(request, 'quality_control/bug_list.html', {'bugs': bugs})

def feature_list(request):
    features = FeatureRequest.objects.all()
    return render(request, 'quality_control/feature_list.html', {'features': features})

def bug_report_detail(request, bug_id):
    bug = get_object_or_404(BugReport, id=bug_id)
    return render(request, 'quality_control/bug_detail.html', {'bug': bug})

def feature_request_detail(request, feature_id):
    feature = get_object_or_404(FeatureRequest, id=feature_id)
    return render(request, 'quality_control/feature_detail.html', {'feature': feature})

def add_bug_report(request):
    if request.method == 'POST':
        form = BugReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality_control:bug_list')
    else:
        form = BugReportForm()

    return render(request, 'quality_control/bug_report_form.html', {'form': form})

def add_feature_request(request):
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality_control:feature_list')
    else:
        form = FeatureRequestForm()

    return render(request, 'quality_control/feature_request_form.html', {'form': form})

def bug_report_update(request, bug_id):
    bug_report = get_object_or_404(BugReport, id=bug_id)
    if request.method == 'POST':
        form = BugReportForm(request.POST, instance=bug_report)
        if form.is_valid():
            form.save()
            return redirect('quality_control:bug_detail', bug_id= bug_report.id)
    else:
        form = BugReportForm(instance=bug_report)
    return render(request, 'quality_control/bug_report_form.html', {'form': form})

def feature_request_update(request, feature_id):
    feature_request = get_object_or_404(FeatureRequest, id=feature_id)
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST, instance=feature_request)
        if form.is_valid():
            form.save()
            return redirect('quality_control:feature_detail', bug_id = feature_request.id)
    else:
        form = FeatureRequestForm(instance=feature_request)
    return render(request, 'quality_control/feature_request_form.html', {'form': form})

def bug_report_delete(request, bug_id):
    bug_report = get_object_or_404(BugReport, id=bug_id)
    bug_report.delete()
    return redirect('quality_control:feature_list')
            
def feature_request_delete(request, feature_id):
    feature_request = get_object_or_404(FeatureRequest, id=feature_id)
    feature_request.delete()
    return redirect('quality_control:feature_list')

#CBV---------------------------------------------------------
class BugReportListView(ListView):
    model = BugReport
    pk_url_kwarg = 'bug_id'  
    template_name = 'quality_control/bug_list.html'
    context_object_name = 'bugs'

class FeatureRequestListView(ListView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'
    template_name = 'quality_control/feature_list.html'
    context_object_name = 'features'

class bug_detail(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'
    template_name = 'quality_control/bug_detail.html'
    context_object_name = 'bug'

class feature_detail(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'
    template_name = 'quality_control/feature_detail.html'
    context_object_name = 'feature'

class BugReportCreateView(CreateView):
    model = BugReport
    form_class = BugReportForm
    pk_url_kwarg = 'bug_id'
    template_name = 'quality_control/bug_report_form.html'
    success_url = reverse_lazy('quality_control:bug_list')

class FeatureRequestCreateView(CreateView):
    model = FeatureRequest
    form_class = FeatureRequestForm
    pk_url_kwarg = 'feature_id'
    template_name = 'quality_control/feature_request_form.html'
    success_url = reverse_lazy('quality_control:feature_list')

class BugReportUpdateView(UpdateView):
    model = BugReport
    pk_url_kwarg = 'bug_id'
    form_class = BugReportForm
    template_name = 'quality_control/bug_update.html'
    context_object_name = 'bug'
    def get_success_url(self):
        return reverse_lazy('quality_control:bug_detail', kwargs={'bug_id': self.object.id})

class FeatureRequestUpdateView(UpdateView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'
    form_class = FeatureRequestForm
    template_name = 'quality_control/feature_update.html'
    context_object_name = 'feature'
    def get_success_url(self):
        return reverse_lazy('quality_control:feature_detail', kwargs={'feature_id': self.object.id})
    
class BugReportDeleteView(DeleteView):
    model = BugReport
    pk_url_kwarg = 'bug_id'
    template_name = 'quality_control/bug_report_delete.html'
    context_object_name = 'bug'
    success_url = reverse_lazy('quality_control:bug_list')

class FeatureRequestDeleteView(DeleteView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'
    template_name = 'quality_control/feature_request_delete.html'
    context_object_name = 'feature'
    success_url = reverse_lazy('quality_control:feature_list')