import os
from .base import *

DEBUG = True  # Temporarily set to True for debugging
SECRET_KEY = os.environ.get("SECRET_KEY", "temporary-development-key")
ALLOWED_HOSTS = ["*"]  # Allow all hosts temporarily for debugging

# Add Whitenoise for static files
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Use SQLite initially
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}
