# Generated by Django 4.2.2 on 2023-06-27 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_task_user_completed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='completed',
            old_name='task',
            new_name='ctask',
        ),
    ]
