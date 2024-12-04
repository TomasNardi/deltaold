import os
import django
from django.contrib.auth.models import User

# Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mi_proyecto.settings')  # Cambia 'mi_proyecto' por el nombre de tu proyecto
django.setup()

# Crear el superusuario
def crear_superusuario():
    username = 'admindeltaold'
    password = 'admin123'  # Cambia esto por una contraseña segura
    email = 'admin@example.com'  # Cambia esto por un email válido
    
    # Verificar si el superusuario ya existe
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)
        print(f"Superusuario {username} creado con éxito.")
    else:
        print(f"El superusuario {username} ya existe.")

# Ejecutar la función
if __name__ == '__main__':
    crear_superusuario()
