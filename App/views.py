from typing import List
from django.http.request import QueryDict
from django.shortcuts import redirect, render, HttpResponse
from django.http import HttpResponse
from App.models import Curso, Profesor
from App.forms import CursoFormulario, ProfesorFormulario

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy



# Create your views here.

def curso(request):

      curso =  Curso(nombre="Analisis del futbol", grupo="111111")
      curso.save()
      documentoDeTexto = f"--->Curso: {curso.nombre}   Grupo: {curso.grupo}"


      return HttpResponse(documentoDeTexto)


def inicio(request):

      return render(request, "inicio.html")



def estudiantes(request):

      return render(request, "App/estudiantes.html")


def deportes(request):

      return render(request, "App/deportes.html")


def cursos(request):

      if request.method == 'POST':

            miFormulario = CursoFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  curso = Curso (nombre=informacion['curso'], grupo=informacion['grupo']) 

                  curso.save()

                  return render(request, "inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= CursoFormulario() #Formulario vacio para construir el html

      return render(request, "cursos.html", {"miFormulario":miFormulario})




def profesores(request):

      if request.method == 'POST':

            miFormulario = ProfesorFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  profesor = Profesor (nombre=informacion['nombre'], apellido=informacion['apellido'],
                   email=informacion['email'], area=informacion['area']) 

                  profesor.save()

                  return render(request, "inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= ProfesorFormulario() #Formulario vacio para construir el html

      return render(request, "profesores.html", {"miFormulario":miFormulario})






def buscar(request):

      if  request.GET["grupo"]:

	      #respuesta = f"Estoy buscando la camada nro: {request.GET['camada'] }" 
            grupo = request.GET['grupo'] 
            cursos = Curso.objects.filter(grupo__icontains=grupo)

            return render(request, "inicio.html", {"cursos":cursos, "grupo":grupo})

      else: 

	      respuesta = "No enviaste datos"

      #No olvidar from django.http import HttpResponse
      return HttpResponse(respuesta)



def leerProfesores(request):

      profesores = Profesor.objects.all() #trae todos los profesores

      contexto= {"profesores":profesores} 

      return render(request, "App/leerProfesores.html",contexto)



def eliminarProfesor(request, profesor_nombre):

      profesor = Profesor.objects.get(nombre=profesor_nombre)
      profesor.delete()
      
      #vuelvo al menú
      profesores = Profesor.objects.all() #trae todos los profesores

      contexto= {"profesores":profesores} 

      return render(request, "App/leerProfesores.html",contexto)



def editarProfesor(request, profesor_nombre):

      #Recibe el nombre del profesor que vamos a modificar
      profesor = Profesor.objects.get(nombre=profesor_nombre)

      #Si es metodo POST hago lo mismo que el agregar
      if request.method == 'POST':

            miFormulario = ProfesorFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  profesor.nombre = informacion['nombre']
                  profesor.apellido = informacion['apellido']
                  profesor.email = informacion['email']
                  profesor.profesion = informacion['area']

                  profesor.save()

                  return render(request, "App/inicio.html") #Vuelvo al inicio o a donde quieran
      #En caso que no sea post
      else: 
            #Creo el formulario con los datos que voy a modificar
            miFormulario= ProfesorFormulario(initial={'nombre': profesor.nombre, 'apellido':profesor.apellido , 
            'email':profesor.email, 'profesion':profesor.profesion}) 

      #Voy al html que me permite editar
      return render(request, "App/editarProfesor.html", {"miFormulario":miFormulario, "profesor_nombre":profesor_nombre})




class CursoList(ListView):

      model = Curso 
      template_name = "App/cursos_list.html"



class CursoDetalle(DetailView):

      model = Curso
      template_name = "App/curso_detalle.html"



class CursoCreacion(CreateView):

      model = Curso
      success_url = "/App/curso/list"
      fields = ['nombre', 'grupo']


class CursoUpdate(UpdateView):

      model = Curso
      success_url = "/App/curso/list"
      fields  = ['nombre', 'grupo']


class CursoDelete(DeleteView):

      model = Curso
      success_url = "/App/curso/list"
     