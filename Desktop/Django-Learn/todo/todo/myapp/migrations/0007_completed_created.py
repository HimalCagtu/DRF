# Generated by Django 4.2.2 on 2023-06-27 09:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_task_due_alter_task_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='completed',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
