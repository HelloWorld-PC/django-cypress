"""URLs configuration exists so we can run tests without an actual Django project.

Django expects ROOT_URLCONF to exist in the test_settings.py.
It is not used by installed instances of this app.
"""

from django.urls import include, path

urlpatterns = [
    path("", include("django_cypress.urls")),
]
