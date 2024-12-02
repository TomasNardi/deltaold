# Generated by Django 5.1.2 on 2024-12-02 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_productos_imagen_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eventos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('direccion', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
                ('link_entradas', models.URLField(blank=True, max_length=500, null=True)),
                ('incluye_entradas', models.BooleanField(default=False)),
            ],
        ),
    ]
