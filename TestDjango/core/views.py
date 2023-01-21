from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def datos(request):
    # contexto={"nombre":"Jorge"}
    hijo = class_persona("Cristiano Ronaldo","38")
    contexto = {"nombre":"Jorge","pariente":hijo}
    return render(request, 'datos.html',contexto)  

class class_persona:
    def __init__(self,nombre, edad):
        self.nombre=nombre
        self.edad=edad
        super().__init__()

