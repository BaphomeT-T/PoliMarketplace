from django.urls import path
from . import views

urlpatterns = [
    path('', views.userView, name='userView'),  
    path('cambiar-estado-producto/<int:producto_id>/', views.cambiar_estado_producto, name='cambiar_estado_producto'),
]
