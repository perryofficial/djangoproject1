from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.home, name="clothes_home"),
    path("clothes_list/", views.clothes_list, name="clothes_list"),
    path("add/", views.add_clothes, name="add_clothes"),
    path("edit/<int:id>/", views.edit_clothes, name='edit_clothes'),
    path("delete/<int:id>/", views.delete_clothes, name='delete_clothes'),
]