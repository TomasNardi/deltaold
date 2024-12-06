from django.urls import path
from . import views

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
    path("singles", views.single, name="singles"),
    path("sellados", views.sellado, name="sellados"),
    path("eventos/", views.evento, name="eventos"),
    path("crearusuario/", views.create_superuser),
]
