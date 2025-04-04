from django.apps import AppConfig
from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

class UsuariosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'usuarios'

    def ready(self):
        # Evita import circular
        from django.db.utils import OperationalError
        try:
            from .initial_users import create_initial_users
            create_initial_users()
        except OperationalError:
            # Evita erro quando ainda não foi feita a migrate
            pass
