from django.urls import path
from . import views


urlpatterns = [
    path("login/", views.login, name="login"),
    path("schemas/", views.list_schema, name="list_schema"),
    path("new-schema/", views.new_schema, name="new_schema"),
    path("schemas/<id>/", views.list_dataset, name="list_dataset"),
]