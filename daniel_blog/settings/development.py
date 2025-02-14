from .base import *

# DEBUG = os.environ.get("DEBUG", "1").lower() in ("true", "1", "yes")
DEBUG = True

ALLOWED_HOSTS = [".vercel.app", "daniel_blog.vercel.app", "daniel-blog-o2te.vercel.app", ".pythonanywhere.com", "localhost", '127.0.0.1']

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "daniel_blog_db"
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')