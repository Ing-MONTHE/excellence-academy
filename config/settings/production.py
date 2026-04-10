from .base import *

# ==============================================================================
# BASE DE DONNÉES (PostgreSQL production)
# ==============================================================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT', default='5432'),
        'CONN_MAX_AGE': 60,  # Connexions persistantes
    }
}

# ==============================================================================
# SÉCURITÉ
# ==============================================================================
DEBUG = False
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_SSL_REDIRECT = True          # Force HTTPS
SESSION_COOKIE_SECURE = True        # Cookie session via HTTPS uniquement
CSRF_COOKIE_SECURE = True           # Cookie CSRF via HTTPS uniquement
X_FRAME_OPTIONS = 'DENY'
SECURE_HSTS_SECONDS = 31536000      # HSTS : 1 an
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# ==============================================================================
# STOCKAGE MÉDIAS (Amazon S3)
# ==============================================================================
AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID', default='')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY', default='')
AWS_STORAGE_BUCKET_NAME = config('AWS_S3_BUCKET', default='')
AWS_S3_REGION_NAME = config('AWS_S3_REGION', default='eu-west-1')
AWS_DEFAULT_ACL = 'private'

if AWS_STORAGE_BUCKET_NAME:
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    MEDIA_URL = f'https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/media/'