# Generated by Django 5.1.2 on 2024-10-23 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.TextField(default='sin descripcion'),
            preserve_default=False,
        ),
    ]
