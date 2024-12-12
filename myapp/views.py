#Importo la funcion de requeriemito de login.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse , JsonResponse
from urllib.parse import urlencode
from django.shortcuts import get_object_or_404
from django.shortcuts import render
#Importo las tablas para manejar los datos que se encuentran ahi.
from .models import Task, Productos , Eventos
#Imoportamos la funcion de renderizado de la web. 
from django.shortcuts import render , redirect
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
    eventos = Eventos.objects.all()
    return render(request, 'eventos.html', {'eventos' : eventos})
    
def productos(request):
    productos = Productos.objects.all()
    carrito_ids = request.session.get('carrito', [])
    
    # Crear un conjunto con los ids de los productos en el carrito para comprobar rápidamente
    carrito_ids_set = set(item['id'] for item in carrito_ids)
    
    return render(request, "tienda.html", {'productos': productos, 'carrito_ids': carrito_ids_set})



def single(request):
    productos = Productos.objects.all()
    carrito_ids = request.session.get('carrito', [])
    carrito_ids_set = set(item['id'] for item in carrito_ids)
    return render(request, "tiendas/singles.html", {'productos': productos, 'carrito_ids': carrito_ids_set})

def sellado(request):
    productos = Productos.objects.all()
    return render(request, "tiendas/sellados.html", {'productos' : productos})

"""def tasks(request, id):
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
            return redirect('index')"""
        
        
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
    
def obtener_cantidad_productos(request):
    carrito = request.session.get("carrito", [])
    cantidad_productos = sum(item["cantidad"] for item in carrito)  
    return JsonResponse({"cantidad_productos": cantidad_productos})
    

def agregar_al_carrito(request):
    if request.method == "POST":
        producto_id = request.POST.get("producto_id")

        # Obtener el producto
        producto = get_object_or_404(Productos, id=producto_id)

        # Verificar que el producto tiene stock disponible
        if not producto.stock:
            return JsonResponse({"success": False, "error": "Producto sin stock."})

        # Inicializar el carrito en la sesión si no existe
        if "carrito" not in request.session:
            request.session["carrito"] = []

        carrito = request.session["carrito"]

        # Verificar si el producto ya está en el carrito
        for item in carrito:
            if item["id"] == producto.id:
                # Eliminar el producto si ya está en el carrito (funcionalidad de toggle)
                carrito.remove(item)
                request.session["carrito"] = carrito
                request.session.modified = True  # Marcar la sesión como modificada
                return JsonResponse({
                    "success": True,
                    "agregado": False,  # Indica que fue eliminado
                    "cantidad_productos": len(carrito),  # Cantidad actualizada en el carrito
                })

        # Agregar el producto al carrito
        carrito.append({
            "id": producto.id,
            "titulo": producto.titulo,
            "precio": float(producto.precio),
            "cantidad": 1,  # Por defecto, agregar 1 unidad
        })

        # Guardar el carrito actualizado en la sesión
        request.session["carrito"] = carrito
        request.session.modified = True  # Asegúrate de marcar la sesión como modificada

        # Responder con el estado actualizado del carrito
        return JsonResponse({
            "success": True,
            "agregado": True,  # Indica que fue agregado
            "cantidad_productos": len(carrito),  # Cantidad actualizada en el carrito
        })

    return JsonResponse({"success": False, "error": "Método no permitido."})



def ver_carrito(request):
    carrito = request.session.get("carrito", [])  # Obtener los productos del carrito desde la sesión

    # Si el carrito está vacío, mostrar un mensaje
    if not carrito:
        return render(request, "tiendas/carrito.html", {"mensaje": "Tu carrito está vacío.", "cantidad_productos": 0})
    
    # Calcular el total de cada producto (precio x cantidad) y el total del carrito
    for item in carrito:
        item["total_producto"] = item["precio"] * item["cantidad"]  # Total por producto
    
    # Calcular el total general del carrito
    total = sum(item["total_producto"] for item in carrito)
    cantidad_productos = sum(item["cantidad"] for item in carrito)  # Cantidad total de productos
    
    # Crear el mensaje de WhatsApp
    mensaje = "Carrito de Compras de Delta Old:\n"
    for item in carrito:
        mensaje += f"{item['titulo']} - $ {item['precio']} x {item['cantidad']} = $ {item['total_producto']}\n"
    
    mensaje += f"\nTotal: $ {total}"  # Añadir el total al final del mensaje
    
    return render(request, "tiendas/carrito.html", {
        "carrito": carrito,
        "total": total,
        "mensaje": mensaje,
        "cantidad_productos": cantidad_productos
    })



def eliminar_del_carrito(request):
    if request.method == "POST":
        producto_id = request.POST.get("producto_id")

        carrito = request.session.get("carrito", [])
        carrito = [item for item in carrito if item["id"] != int(producto_id)]

        request.session["carrito"] = carrito
        request.session.modified = True

        return JsonResponse({"status": "success"})  # Respuesta para confirmar eliminación
    return JsonResponse({"error": "Método no permitido."}, status=405)


#Lo armo para enviar por whats app el pedido.
def procesar_compra(request):
    carrito = request.session.get("carrito", [])
    if not carrito:
        return JsonResponse({"error": "El carrito está vacío."})

    # Crear el mensaje para WhatsApp
    mensaje = "¡Hola! Quiero comprar los siguientes productos:\n\n"
    for item in carrito:
        mensaje += f"- {item['titulo']} (x{item['cantidad']}): ${item['precio']} c/u\n"
    total = sum(item["precio"] * item["cantidad"] for item in carrito)
    mensaje += f"\nTotal: ${total}"

    # URL de WhatsApp
    telefono_vendedor = "541152203378"  # Cambia al número del vendedor
    url = f"https://wa.me/{telefono_vendedor}?{urlencode({'text': mensaje})}"

    return JsonResponse({"url": url})


def eliminar_de_tienda(request):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        producto_id = request.POST.get('producto_id')

        if producto_id:
            try:
                # Obtener el carrito de la sesión
                carrito = request.session.get('carrito', [])

                # Buscar el producto y eliminarlo
                carrito = [producto for producto in carrito if producto['id'] != int(producto_id)]

                # Guardar el carrito actualizado en la sesión
                request.session['carrito'] = carrito

                # Responder correctamente
                return JsonResponse({'success': True})

            except Exception as e:
                return JsonResponse({'error': str(e)}, status=400)

        return JsonResponse({'error': 'Producto no encontrado'}, status=400)

    return JsonResponse({'error': 'Solicitud inválida'}, status=400)
