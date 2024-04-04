from django.contrib import admin
from .models import BugReport, FeatureRequest
from django.contrib import messages

def change_status(self, request, queryset):
    queryset.update(status='closed')
@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'task', 'status', 'priority', 'created_at')
    list_filter = ('project', 'status', 'priority')
    search_fields = ('title', 'description')
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'project', 'task', 'status', 'priority')
        }),
    )
    actions = ['change_status']

    def change_status(self, request, queryset):
        updated = queryset.update(status='In_progress')
        self.message_user(request, f"{updated} bug reports were successfully updated.", messages.SUCCESS)
    change_status.short_description = "Mark selected reports as 'In progress'"
    
    
@admin.register(FeatureRequest)
class FeatureRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'task', 'status', 'priority', 'created_at')
    list_filter = ('project', 'status', 'priority')
    search_fields = ('title', 'description')
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'project', 'task', 'status', 'priority')
        }),
    )