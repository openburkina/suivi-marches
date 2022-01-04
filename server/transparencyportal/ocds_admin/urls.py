from django.urls import path
from ocds_admin.views import index, UploadFileView

urlpatterns = [
    path("", index, name="ocds-admin-index"),
    path("import/", UploadFileView.as_view(), name="import-data")
]
