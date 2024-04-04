from django.db import models
from tasks.models import Project, Task
# Create your models here.
class BugReport(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(
        Project,
        related_name='BugReport',
        on_delete=models.CASCADE
    )
    task =  models.ForeignKey(
        Task,
        related_name='BugReport',
        on_delete=models.SET_NULL,
        null=True,
    ) 
    STATUS_CHOICES = [
        ('New', 'Новая'),
        ('In_progress', 'В работе'),
        ('Completed', 'Завершена'),
    ]
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='New',
    )
    priority = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=1)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

class FeatureRequest(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(
        Project,
        related_name='FeatureRequest',
        on_delete=models.CASCADE
    )
    task =  models.ForeignKey(
        Task,
        related_name='FeatureRequest',
        on_delete=models.SET_NULL,
        null=True,
    )
    STATUS_CHOICES = [
        ('Approval', 'Рассмотрение'),
        ('Approved', 'Принято'),
        ('Denied', 'Отклонено'),
    ]
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='Approval',
    )
