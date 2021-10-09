from django.shortcuts import render,get_object_or_404
from . models import Categoria, Producto
from tienda.carrito import Cart

# Create your views here.
def index(request):
    product_list = Producto.objects.order_by('nombre')[:6]
    catego = Categoria.objects.all()
    context={
        'product_list':product_list,
        'catego':catego
    }
    return render(request,'index.html',context)

def producto(request,producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    catego = Categoria.objects.all()
    return render(request,'producto.html',{'producto':producto,'catego':catego})

def categoria(request,categoria_id):
    catego = Categoria.objects.all()
    categoria = Producto.objects.filter(Categoria=categoria_id)
    return render(request,'categorias.html',{'categoria':categoria,'catego':catego})



def agregarCarrito(request,producto_id):
    objProducto = Producto.objects.get(id=producto_id)
    carritoProducto = Cart(request)
    carritoProducto.add(objProducto,1)
    print(request.session.get("cart"))
    return render(request,'carrito.html')

def eliminarProductoCarrito(request,producto_id):
    objProducto = Producto.objects.get(id=producto_id)
    carritoProducto = Cart(request)
    carritoProducto.remove(objProducto)
    print(request.session.get("cart"))
    return render(request,'carrito.html')

def limpiarCarrito(request):
    CarritoProducto = Cart(request)
    CarritoProducto.clear()
    print(request.session.get("cart"))
    return render(request,'carrito.html')

def carrito(request):
    print(request.session.get("cart"))
    return render(request,'carrito.html')

