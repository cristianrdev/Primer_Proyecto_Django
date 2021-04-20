from django.shortcuts import render, HttpResponse, redirect # agrega redirección a la declaración de importación
# def index(request):
    # return HttpResponse("this is the equivalent of @app.route('/')!")
    # return redirect('/blogs')
    # return redirect('metodo1')

# Create your views here.

def root(request):
	return redirect('/blogs')

def index(request):
    return HttpResponse("placeholder para luego mostrar una lista de todos los blogs")

def new(request):
    return HttpResponse("placeholder para mostrar un nuevo formulario para crear un nuevo blog")

def create(request):
    return redirect('/')
def show(request, number):
    return HttpResponse(f"placeholder para mostrar el blog numero: {number}")

def edit(request, number):
    return HttpResponse(f"placeholder para editar el blog {number}")

def destroy(request, number):
    return HttpResponse(f"placeholder para eliminar el blog {number}")
