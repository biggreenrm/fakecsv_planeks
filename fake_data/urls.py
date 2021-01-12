from django.urls import path
from . import views


urlpatterns = [
    path("login/", views.login, name="login"),
    path("schemas/", views.list_schema, name="list_schema"),
    path("new-schema/", views.new_schema, name="new_schema"),
    path("schemas/<id>/", views.list_dataset, name="list_dataset"),
    path("schemas/<id>/edit/", views.edit_schema, name="edit_schema"),
    path("schemas/<id>/delete/", views.delete_schema, name="delete_schema"),
]