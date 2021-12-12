from django.conf import settings
from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter

from transparencyportal.users.api.views import UserViewSet
from transparencyportal.ocds_release.views import RecordViewSet, ReleaseViewSet
from transparencyportal.ocds_tender.views import BuyerViewSet
from transparencyportal.ocds_planning.views import PlanningViewSet

from transparencyportal.ocds_release.urls import buyer_urlpatterns, record_urlpatterns, release_urlpatterns

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("records", RecordViewSet)
router.register("releases", ReleaseViewSet)
router.register("buyers", BuyerViewSet)
router.register("plannings", PlanningViewSet)

app_name = "api"
urlpatterns = router.urls

urlpatterns += [
    path("tenders/", include("ocds_tender.urls")),
    path("buyers/", include(buyer_urlpatterns)),
    path("records/", include(record_urlpatterns)),
    path("releases/", include(release_urlpatterns)),
    path('docs/', include("api_doc.urls")),
]
