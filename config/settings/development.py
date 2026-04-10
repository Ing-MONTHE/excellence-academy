from .base import *

# ==============================================================================
# BASE DE DONNÉES (PostgreSQL local)
# ==============================================================================
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("DB_NAME"),
        "USER": config("DB_USER"),
        "PASSWORD": config("DB_PASSWORD"),
        "HOST": config("DB_HOST", default="localhost"),
        "PORT": config("DB_PORT", default="5432"),
    }
}

# ==============================================================================
# DEBUG
# ==============================================================================
DEBUG = True
CORS_ALLOW_ALL_ORIGINS = True  # Autorise tout en développement

# ==============================================================================
# LOGS (affiche tout dans le terminal)
# ==============================================================================
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {"class": "logging.StreamHandler"},
    },
    "root": {
        "handlers": ["console"],
        "level": "DEBUG",
    },
}
