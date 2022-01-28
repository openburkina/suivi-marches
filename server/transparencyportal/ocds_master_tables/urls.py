from django.urls import path

from .views import FacebookPublishView, RegionListView

urlpatterns = [
        path(r'publish', FacebookPublishView.as_view()),
]

region_urlpatterns = [
        path(r'', RegionListView.as_view(), name='region-list')
]