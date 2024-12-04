#Importo la funcion de requeriemito de login.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse , JsonResponse
from django.shortcuts import get_object_or_404
#Importo las tablas para manejar los datos que se encuentran ahi.
from .models import Project , Task, Productos
#Imoportamos la funcion de renderizado de la web. 
from django.shortcuts import render , redirect
from .forms import CreateNewTasks 
#Formulario para crear usuario.
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
#Funcionalidad para agregar Usuarios
from django.contrib.auth.models import User
#Importo la funcionalidad Django - Cookie
from django.contrib.auth import login , logout , authenticate
from django.db import IntegrityError

# Create your views here.
def index(request):
    info = Task.objects.all().order_by('-user')
    return render(request , 'index.html', {'info' : info })

#Sign Up - Creacion de usuario.
def crear_usuario(request):
    if request.method == 'GET':
        return render(request, 'crear_usuario.html', {
            'formulario_crear_usuario' : UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                username = request.POST['username'],
                password= request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('index')
            except IntegrityError:
                    return render(request, 'crear_usuario.html', {
                    'formulario_crear_usuario' : UserCreationForm,
                    'error': 'Error - El usuario se encuentra registrado'})
                
        return render(request, 'crear_usuario.html', {
                    'formulario_crear_usuario' : UserCreationForm,
                    'error': 'Las contraseñas no coinciden'})
            
#@login_required
def evento(request):
    return render(request, 'eventos.html')
    
def productos(request):
    productos = Productos.objects.all()
    return render(request, "tienda.html", {'productos' : productos})


def tasks(request, id):
    task = get_object_or_404(Task , id = id)
    return render(request , 'tasks/tasks.html', {'task' : task})

#Paso el form - que importo como diccionario para usar en el html. (Es una funcion ->() ).
def tasks_form(request):
    #Tomo los parametros del formulario. Creo objetos en tabla Task.
    #Importante : Las variables deben conicindir con los campos de los modelos. 
    Task.objects.create(title = request.GET['title'], 
    description = request.GET['description'],
    project_id =3)
    return render(request, 'tasks_form.html', {'form' : CreateNewTasks()})

    
def signout(request):
    logout(request)
    return redirect('index')
        
def signin(request):
    if request.method == 'GET':
        return render(request, 'login.html', {'form' : 
            AuthenticationForm})
    else: 
        user = authenticate(
            request , username = request.POST['username'], password = request.POST['password']
        )
        if user is None:
            return render(request, 'login.html', {'form' : 
                AuthenticationForm, 'error' : 'El usuario o contraseña son incorrectos.'})
        else:
            login(request , user)
            return redirect ('index')
      
def actualizar(request, id):
    #Cargo los datos para ambos casos
    task = get_object_or_404(Task, id=id , user = request.user) 
    
    if request.method == 'GET':
        # Obtener la tarea desde la base de datos 
        # Armo el form
        form = CreateNewTasks(initial={
            'title': task.title,
            'description': task.description
        })
        return render(request, 'tasks/update_form.html', {'task': task, 'form': form})
    else:
        form = CreateNewTasks(request.POST)  
        if form.is_valid():
            # si el formulario es válido, debes actualizar la tarea en la base de datos
            task.title = form.cleaned_data['title']
            task.description = form.cleaned_data['description']
            print(f"El titulo es {task.title} y su descripcion {task.description}")
            task.save()  # Guardar la tarea actualizada
            return redirect('index') 
        
def borrar_tarea(request, id):
    #Traigo los datos de la BD.
        task = get_object_or_404(Task, id=id , user = request.user) 
        
        if request.method == 'POST':
            print(f"Hago delete de la tarea con el siguiente id -> {id}")
            #Funcion delete de Django, task coma el valor de id = id.
            task.delete() 
            return redirect('index')
        
        
def create_superuser(request):
    username = 'admindeltaold'
    password = 'admin1999'  
    email = 'admin@example.com'  
    
    # Crear el superusuario si no existe
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)
        return HttpResponse("Superusuario creado con éxito.")
    else:
        return HttpResponse("El superusuario ya existe.")