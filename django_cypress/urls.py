from django.urls import path

from .views import CSRFTokenView, ManageView

urlpatterns = [
    path("__cypress__/manage/", ManageView.as_view(), name="manage-view"),
    path("__cypress__/csrftoken/", CSRFTokenView.as_view(), name="csrftoken-view"),
]
