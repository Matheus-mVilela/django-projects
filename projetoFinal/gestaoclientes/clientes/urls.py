from django.urls import path
from .views import person_list
from .views import person_new
from .views import person_update
from .views import person_delete
from .views import return_list
from .views import back_home

urlpatterns = [
    path("list/", person_list, name="person_list"),
    path("new/", person_new, name="person_new"),
    path("update/<int:id>/", person_update, name="person_update"),
    path("delete/<int:id>/", person_delete, name="person_delete"),
    path("listreturn/", return_list, name="return_list"),
    path("backhome/", back_home, name="back_home"),
]



