from django.db import migrations

def create_superuser(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
    username = "deltaoldadmin",
    email = "admin@example.com",
    password = "chile1996"
        )

class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_eventos'),
    ]

    operations = [
        migrations.RunPython(create_superuser),
    ]