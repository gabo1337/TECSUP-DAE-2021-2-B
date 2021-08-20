from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("coloque en la url la operacion suma,resta,multiplicacion seguidamente coloque los dos numeros")

def suma(request, num1, num2):
    suma = num1 + num2
    resultado = str(suma)
    return HttpResponse(str(num1)+"+"+str(num2)+"= "+resultado)

def resta(request, num1, num2):
    resta = num1 - num2
    resultado = str(resta)
    return HttpResponse(str(num1)+"-"+str(num2)+"= "+resultado)

def multiplicacion(request, num1, num2):
    multiplicacion = num1 * num2
    resultado = str(multiplicacion)
    return HttpResponse(str(num1)+"-"+str(num2)+"= "+resultado)
