from django.shortcuts import render, render_to_response
from models import Persona, Compra, Producto
# Create your views here.

def listarPersona(request):

    if request.GET.get('id'):

        idPersona = request.GET.get('id')

        p = p.objects.filter(id=idPersona)


    else:

        p = Persona.objects.all()

    return render_to_response('persona.html', { 'personas' : p })


def listarProducto(request):

    if request.GET.get('id'):

        idProducto = request.GET.get('id')

        p = p.objects.filter(id=idProducto)


    else:

        p = Producto.objects.all()

    return render_to_response('producto.html', { 'productos' : p })

def listarCompra(request):

    if request.GET.get('id'):

        idCompra = request.GET.get('id')

        p = p.objects.filter(id=idCompra)


    else:

        p = Compra.objects.all()

    return render_to_response('compra.html', { 'compras' : p })
