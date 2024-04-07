from django.urls import path
from quality_control import views
from .views import add_bug_report, add_feature_request

app_name = 'quality_control'

urlpatterns = [
    path('', views.index, name='index'),
    path('bugs/', views.bug_list, name='bug_list'),
    path('features/', views.feature_list, name='feature_list'),
    path('bugs/<int:bug_id>/', views.bug_detail.as_view(), name='bug_detail'),
    path('features/<int:feature_id>/', views.feature_detail.as_view(), name='feature_detail'),
    path('add_bug_report/', add_bug_report, name='add_bug_report'),
    path('add_feature_request/', add_feature_request, name='add_feature_request'),
]