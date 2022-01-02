from django.urls import path
from ocds_admin.views import import_data_view

urlpatterns = [
    path("perform/", import_data_view, name="import-data")
]
