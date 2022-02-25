from django.shortcuts import redirect, render, get_object_or_404
from .forms import Producto_Form
from django.contrib import messages
from .models import*
from django.db.models import Q
# Create your views here.
def main(request):
     busqueda = request.GET.get("buscar")
     producto = Productos.objects.all()


     if busqueda:
          producto = Productos.objects.filter(
               Q(nombres_icontains = busqueda) |
               Q(precio_icontains = busqueda) |
               Q(descripcion_icontains = busqueda)
          ).distinc()
          
     return render(request,'store/main.html', {'producto': producto })
                      


def nuevo_producto(request):
     data = {
          'form':Producto_Form()
     }
     if request.method == 'POST':
          form = Producto_Form(request.POST, request.FILES)
          if form.is_valid():
               form.save()
               
               
          else:
               data["from"] = form     
               
     return render(request,'store/nuevo_producto.html',data)


def lista_produtos(request):

    producto = Productos.objects.all()
    categorias = Categoria.objects.all()
      
          
    data = {'producto' : producto,'categorias' :categorias}
    return render(request,'store/lista_productos.html', data)


def editar_produtos(request, id ):
     productos = get_object_or_404(Productos, id=id)
     categorias = Categoria.objects.all()

     data = {
          'form':Producto_Form(instance=productos), 'categorias': categorias
     }
     if request.method == 'POST':
          form = Producto_Form(data=request.POST, instance=productos, files=request.FILES)
          if form.is_valid():
               form.save()
               return redirect  ("lista" )
               
          data ['form'] = 'form'

     return render(request, 'store/modificar.html',data) 



def elimanar_producto(request, id):
     productos = get_object_or_404(Productos, id=id)
     productos.delete()
     messages.success(request, 'Producto Eliminado ')
     return redirect  ("lista" )
