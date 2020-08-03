from django.urls import path 
from .views import homepage, logout_view


urlpatterns = [
    path('', homepage, name='homepage'),
    path('logout/', logout_view, name='logout'),
]  