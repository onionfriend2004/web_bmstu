# Generated by Django 5.0.3 on 2024-04-04 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quality_control', '0002_alter_bugreport_priority_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FeatureRequest',
        ),
    ]
