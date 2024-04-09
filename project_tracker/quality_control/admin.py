from django.contrib import admin
from .models import BugReport, FeatureRequest
from django.contrib import messages

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
    actions = ['change_status_to_inprogress', 'change_status_to_closed']

    def change_status_to_inprogress(self, request, queryset):
        updated = queryset.update(status='In_progress')
        self.message_user(request, f"{updated} bug reports were successfully updated.", messages.SUCCESS)
    change_status_to_inprogress.short_description = "Mark selected reports as 'In progress'"

    def change_status_to_closed(self, request, queryset):
        updated = queryset.update(status='Closed')
        self.message_user(request, f"{updated} bug reports were successfully updated.", messages.SUCCESS)
    change_status_to_closed.short_description = "Mark selected reports as 'Closed'"
    
    
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