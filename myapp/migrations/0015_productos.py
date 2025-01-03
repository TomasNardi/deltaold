# Generated by Django 5.1.2 on 2024-11-29 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_task_creado_alter_task_fecha'),
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.BooleanField(default=False)),
            ],
        ),
    ]
