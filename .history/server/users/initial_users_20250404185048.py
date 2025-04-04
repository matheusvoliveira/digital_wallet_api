from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth import get_user_model

@receiver(post_migrate)
def create_initial_users(sender, **kwargs):
    Usuario = get_user_model()

    usuarios_iniciais = [
        {"nome": "Matheus", "email": "matheus@email.com", "password": "senha123"},
        {"nome": "Joana", "email": "joana@email.com", "password": "senha123"},
        {"nome": "Carlos", "email": "carlos@email.com", "password": "senha123"},
        {"nome": "Ana", "email": "ana@email.com", "password": "senha123"},
        {"nome": "Lucas", "email": "lucas@email.com", "password": "senha123"},
    ]

    for dados in usuarios_iniciais:
        if not Usuario.objects.filter(email=dados["email"]).exists():
            Usuario.objects.create_user(**dados)
            print(f"[✔] Usuário criado: {dados['email']}")
