from django.conf import settings
from django.urls import include, path
from rest_framework.routers import DefaultRouter, SimpleRouter

from transparencyportal.ocds_planning.views import PlanningViewSet
from transparencyportal.ocds_release.urls import (
    buyer_urlpatterns,
    record_urlpatterns,
    release_urlpatterns,
)
from transparencyportal.ocds_master_tables.urls import (
    region_urlpatterns
)
from transparencyportal.ocds_release.views import (
    ReleaseViewSet,
    TargetViewSet,
)
from transparencyportal.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("targets", TargetViewSet)
router.register("releases", ReleaseViewSet)
router.register("plannings", PlanningViewSet)

app_name = "api"
urlpatterns = router.urls

urlpatterns += [
    path("tenders/", include("ocds_tender.urls")),
    path("facebook/", include("ocds_master_tables.urls")),
    path("buyers/", include(buyer_urlpatterns)),
    path("records/", include(record_urlpatterns)),
    path("releases/", include(release_urlpatterns)),
    path("regions/", include(region_urlpatterns)),
    path('docs/', include("api_doc.urls")),
]
