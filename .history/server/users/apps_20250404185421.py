from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        from django.db.utils import OperationalError
        try:
            from .initial_users import create_initial_users
            create_initial_users()
        except OperationalError:
            # Evita erro caso as tabelas ainda não existam
            pass