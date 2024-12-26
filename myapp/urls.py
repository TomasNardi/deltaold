from django.urls import path
from . import views
from .views import google_verification

urlpatterns = [
    # path("tasks/<int:id>/", views.tasks, name="tasks"),
    # path("tasks_form", views.tasks_form, name="tasks_form"),
    # path("registrarse", views.crear_usuario),
    # path("update/<int:id>/", views.actualizar, name="update"),
    # path("update/<int:id>/delete", views.borrar_tarea, name="delete"),
    # path("logout", views.signout, name="logout"),
    # path("login", views.signin, name="login"),
    # path("crear_usuario", views.crear_usuario, name="nuevo_usuario"),
    path("", views.index, name="index"),
    path("productos", views.productos, name="tienda"),
    path("singles/", views.single, name="singles"),
    path("sellados/", views.sellado, name="sellados"),
    path("gradeadas/", views.certificadas, name="gradeadas"),
    path("eventos/", views.evento, name="eventos"),
    path("crearusuario/", views.create_superuser),
    path("ver_carrito/", views.ver_carrito, name="ver_carrito"),
    path("agregar_al_carrito/", views.agregar_al_carrito, name="agregar_al_carrito"),
    path("eliminar_del_carrito/", views.eliminar_del_carrito, name="eliminar_del_carrito"),
    path("eliminar_de_tienda/", views.eliminar_de_tienda, name="eliminar_de_tienda"),
    path("api/cantidad-productos/", views.obtener_cantidad_productos, name="api_cantidad_productos"),
    path("api/cantidad-productos/", views.obtener_cantidad_productos, name="api_cantidad_productos"),
    path('googlec4d88a0b592d5be2.html', google_verification),
    
    #test carrito

    path('buscar', views.buscar_productos, name='buscar_productos'),
]
