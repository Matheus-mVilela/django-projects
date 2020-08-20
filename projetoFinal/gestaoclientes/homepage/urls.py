from django.urls import path 
from .views import homepage, logout_view
from .views import cadastroclientes


urlpatterns = [
    path('', homepage, name='homepage'),
    path('logout/', logout_view, name='logout'),
    path('cadastro-clientes/', cadastroclientes , name='cadastroclientes'),
]  