from django.db import migrations

def poblar_sectores(apps, schema_editor):
    Sector = apps.get_model('signup', 'Sector')
    sectores = [
        "Centro Histórico",
        "La Floresta",
        "Quitumbe",
        "Cumbayá",
        "Carcelén",
        "El Condado",
        "Chimbacalle"
    ]

    for nombre in sectores:
        Sector.objects.get_or_create(nombre=nombre)

class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0001_initial'),  # Asegúrate de que dependa de la migración inicial
    ]

    operations = [
        migrations.RunPython(poblar_sectores),
    ]
