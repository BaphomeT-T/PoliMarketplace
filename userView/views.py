from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from publish.models import Producto

@login_required
def userView(request):
    user = request.user
    user_articles = Producto.objects.filter(usuario=user)

    if request.method == 'POST':
        producto_id = request.POST.get('producto_id')
        action = request.POST.get('action')  # "marcar_como_vendido" o "enlistar_otra_vez"

        producto = get_object_or_404(Producto, id=producto_id, usuario=user)

        if action == 'marcar_como_vendido' and producto.venta_estado == 'EnVenta':
            producto.venta_estado = 'Vendido'
            producto.save()
            messages.success(request, "El producto se ha marcado como vendido")
        elif action == 'enlistar_otra_vez' and producto.venta_estado == 'Vendido':
            producto.venta_estado = 'EnVenta'
            producto.save()
            messages.success(request, "El producto se ha enlistado otra vez")
        else:
            messages.error(request, "Acción no válida para este producto")

        return redirect('userView')  # Recargar la página para reflejar los cambios

    context = {
        'name': f"{user.first_name} {user.last_name}",
        'sector': user.sector.name if user.sector else '',
        'user_articles': user_articles,
    }

    return render(request, 'userView/userView.html', context)

@login_required
def cambiar_estado_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id, usuario=request.user)

    if producto.venta_estado == 'EnVenta':
        producto.venta_estado = 'Vendido'
        messages.success(request, "El producto se ha marcado como vendido")
    elif producto.venta_estado == 'Vendido':
        producto.venta_estado = 'EnVenta'
        messages.success(request, "El producto se ha enlistado otra vez")
    else:
        messages.error(request, "Estado no válido")

    producto.save()
    return redirect('userView')  # Asegúrate de que 'userView' está correctamente definido en tu urls.py
