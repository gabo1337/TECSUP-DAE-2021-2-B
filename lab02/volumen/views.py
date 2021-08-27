from django.shortcuts import render
import math

# Create your views here.
def index(request):
    context = {
        'titulo' : "Volumen del cilindro",
    }
    return render(request,'cilindro/datos.html',context)

def volumen(request):
    altura = request.POST["altura"]
    diametro = request.POST["diametro"]
    
    
    #radio
    r=float(diametro)/2
    #area de la base
    area=math.pi*(r**2)
    vol = float(area)*float(altura)


    context = {
        'titulo' : "el Volumen del cilindro es",
        'volumen': vol,
    }
    return render(request,'cilindro/respuesta.html',context)