from django.shortcuts import render
from publish.models import Categoria, Producto, Estado
from .forms import FiltroProductoForm

def lista_productos_view(request):
    # Obtener las categorías y estados
    categorias = Categoria.objects.all()
    estados = Estado.objects.all()
    
    # Obtener los productos filtrados por zona (sector del usuario) y por categoría
    user = request.user
    if user.is_authenticated:
        productos_sector = Producto.objects.filter(sector=user.sector, venta_estado="EnVenta").exclude(usuario=user)
        otros_productos = Producto.objects.exclude(sector=user.sector).filter(venta_estado="EnVenta").exclude(usuario=user)
    else:
        productos_sector = Producto.objects.none()
        otros_productos = Producto.objects.filter(venta_estado="EnVenta")

    # Filtrar los productos por la categoría seleccionada
    categoria_id = request.GET.get('categoria_id', None)
    if categoria_id:
        productos_sector = productos_sector.filter(categoria_id=categoria_id)
        otros_productos = otros_productos.filter(categoria_id=categoria_id)

    estado_id = request.GET.get('estado_id', None)
    if estado_id:
        productos_sector = productos_sector.filter(estado_id=estado_id)
        otros_productos = otros_productos.filter(estado_id=estado_id)
        
    # Precio
    precio_min = request.GET.get('precio_min', None)
    precio_max = request.GET.get('precio_max', None)
    if precio_min: 
        try: 
            precio_min = float(precio_min)
            productos_sector = productos_sector.filter(precio__gte=precio_min)
            otros_productos = otros_productos.filter(precio__gte=precio_min)   
        except ValueError:
            pass
    if precio_max:
        try: 
            precio_max = float(precio_max)
            productos_sector = productos_sector.filter(precio__lte=precio_max)
            otros_productos = otros_productos.filter(precio__lte=precio_max)
        except ValueError:
            pass

    # Nombre
    query = request.GET.get('q')
    if query: 
        productos_sector = productos_sector.filter(titulo__icontains=query)
        otros_productos = otros_productos.filter(titulo__icontains=query)
        
    # Pasamos los productos filtrados al contexto
    context = {
        'productos_sector': productos_sector,
        'otros_productos': otros_productos,
        'categorias': categorias,
        'estados': estados,
        'query': query,
    }

    return render(request, 'mainPage/mainPage.html', context)
