from django.urls import path

from .views import FacebookPublishView, RegionListView, RegionRecordListView

urlpatterns = [
        path(r'publish', FacebookPublishView.as_view()),
]

region_urlpatterns = [
        path(r'', RegionListView.as_view(), name='region-list'),
        path(r'<int:region_id>/records', RegionRecordListView.as_view(), name='region-record-list')
]