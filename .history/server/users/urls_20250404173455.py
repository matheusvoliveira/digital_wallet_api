


from django.urls import path
from .views import (
    UsuarioCreateView, LoginView, UsuarioDetailView, 
    ListaUsuariosView, atualizar_saldo, transferir_saldo
)

urlpatterns = [
    path("registrar/", UsuarioCreateView.as_view(), name="registrar"),
    path("login/", LoginView.as_view(), name="login"),
    path("me/", UsuarioDetailView.as_view(), name="me"),
    path("usuarios/", ListaUsuariosView.as_view(), name="lista-usuarios"),
    path("usuarios/<int:pk>/saldo/", atualizar_saldo, name="atualizar-saldo"),
    path("transferir/", transferir_saldo, name="transferir-saldo"),
]
