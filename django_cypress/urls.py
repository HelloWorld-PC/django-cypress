from django.urls import path

from .views import CSRFTokenView, ManageView, MigrateView, RefreshDatabaseView

urlpatterns = [
    path("__cypress__/manage/", ManageView.as_view(), name="manage-view"),
    path(
        "__cypress__/refreshDatabase/",
        RefreshDatabaseView.as_view(),
        name="refresh-database-view",
    ),
    path("__cypress__/migrate/", MigrateView.as_view(), name="migrate-view"),
    path("__cypress__/csrftoken/", CSRFTokenView.as_view(), name="csrftoken-view"),
]
