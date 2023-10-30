from django.urls import path
from .views import ClientesView
from .views import ClienteAddView
urlpatterns = [
    path('clientes', ClientesView.as_view(), name='clientes'),
    path('cliente/adicionar/', ClienteAddView.as_view(), name='cliente_adicionar'),
]