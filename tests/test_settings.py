SECRET_KEY = "fake-key"
INSTALLED_APPS = [
    "tests",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "testing",
    }
}

ROOT_URLCONF = "tests.urls"

INSTALLED_APPS = ["django.contrib.contenttypes", "django.contrib.auth"]
