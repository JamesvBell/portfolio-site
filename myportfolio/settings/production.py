import os
from .base import *

DEBUG = False
SECRET_KEY = os.environ.get("SECRET_KEY")
ALLOWED_HOSTS = ["*.onrender.com", "yourdomain.com"]  # Update with your domain later

# Add this section for port binding
PORT = int(os.environ.get("PORT", 8000))

# Use SQLite initially
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}
