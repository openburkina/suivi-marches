from django.conf import settings
from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter

from transparencyportal.users.api.views import UserViewSet
from transparencyportal.ocds_release.views import RecordViewSet, ReleaseViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("records", RecordViewSet)
router.register("releases", ReleaseViewSet)


app_name = "api"
urlpatterns = router.urls

urlpatterns += [
    path("tenders/", include("ocds_tender.urls")),
    path("outputs/", include("ocds_release.urls")),
]
