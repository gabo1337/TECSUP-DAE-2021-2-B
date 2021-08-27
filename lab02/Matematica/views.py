from django.shortcuts import render
def index(request):
    context = {
        'titulo' : "Operaciones",
    }
    return render(request,'operaciones/operacion.html',context)


def solucion(request):
    operacion = request.POST["select"]
    numero1 = request.POST["dato1"]
    numero2 = request.POST["dato2"]
    #si le colocas coma a operacion numero1 y numero2 se convierten en tuplas 
    if(operacion=="suma"):
        respuesta = int(numero1)+int(numero2)
    elif(operacion=="resta"):
        respuesta = int(numero1)-int(numero2)
    elif(operacion=="multiplicacion"):
        respuesta = int(numero1)*int(numero2)    

    
    context={
        'titulo': "Respuesta",
        'numero1': numero1,
        'numero2': numero2,
        'operacion': operacion,
        'respuesta': respuesta,

    }
    
    return render(request,'operaciones/solucion.html',context)
    

# Create your views here.
