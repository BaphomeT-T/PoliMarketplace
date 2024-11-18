from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Usuario, Sector

def signup_views(request):
    if request.method == 'POST':
        # Obtén los datos del formulario
        nombre = request.POST.get('first_name')
        apellido = request.POST.get('last_name')
        fecha_nacimiento = request.POST.get('birth_date')
        genero = request.POST.get('gender')
        sector_id = request.POST.get('sector')
        cedula = request.POST.get('cedula')
        contrasena = request.POST.get('password')

        # Validaciones adicionales si es necesario
        if not sector_id:
            messages.error(request, "Debe seleccionar un sector.")
            return redirect('signup')

        # Busca el sector seleccionado
        try:
            sector = Sector.objects.get(id=sector_id)
        except Sector.DoesNotExist:
            messages.error(request, "El sector seleccionado no existe.")
            return redirect('signup')

        # Crea el usuario
        Usuario.objects.create(
            Nombre=nombre,
            Apellido=apellido,
            Fecha_Nacimiento=fecha_nacimiento,
            Sexo=genero,
            Cedula=cedula,
            Contrasenia=contrasena,
            sector=sector
        )
        messages.success(request, "Usuario registrado correctamente.")
        return redirect('login')  # Cambia 'login' por la URL que desees

    # Si es GET, carga los sectores
    sectores = Sector.objects.all()
    return render(request, 'signup/signup.html', {'sectores': sectores})
