
from django.db import models, transaction
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password

class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("O email é obrigatório")
        email = self.normalize_email(email)
        extra_fields.setdefault("saldo", 1000.0)  # Define saldo padrão caso não seja informado
        user = self.model(email=email, **extra_fields)
        if password:
            user.set_password(password)  # Armazena a senha em hash
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, password, **extra_fields)

class Usuario(AbstractBaseUser):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  
    data_nascimento = models.DateField(null=True, blank=True)
    saldo = models.FloatField(default=1000.0)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # Para controle de admin

    objects = UsuarioManager()
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["nome"]

    def save(self, *args, **kwargs):
        if self.password and not self.password.startswith('pbkdf2_sha256'):
            self.password = make_password(self.password)  # Hash da senha antes de salvar
        super().save(*args, **kwargs)

    def transferir_saldo(self, destinatario, valor):
        """
        Transfere saldo do usuário atual para outro usuário.
        """
        if valor <= 0:
            raise ValueError("O valor da transferência deve ser maior que zero")

        if self.saldo < valor:
            raise ValueError("Saldo insuficiente para a transferência")

        with transaction.atomic():  # Garante que ambas as operações ocorram juntas
            self.saldo -= valor
            destinatario.saldo += valor
            self.save()
            destinatario.save()

    def __str__(self):
        return self.nome
