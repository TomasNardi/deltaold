from django import forms

class CreateNewTasks(forms.Form):
    title = forms.CharField(label="Titulo de tarea", max_length= 200)
    description = forms.CharField(label= "Descripcion de la tarea")
    widget = forms.Textarea()

class Crear_Proyecto(forms.Form):
    name = forms.CharField( label= "Nombre del proyecto" ,max_length=200)