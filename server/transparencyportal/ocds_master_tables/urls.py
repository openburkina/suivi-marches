from django.urls import path

from .views import FacebookPublishView, RegionListView, RegionRecordListView, RegionRecordNumberByStatusYearView, RegionRecordValueByGenericView, RegionRecordValueEvolutionBySectorView

urlpatterns = [
        path(r'publish', FacebookPublishView.as_view()),
]

region_urlpatterns = [
        path(r'', RegionListView.as_view(), name='region-list'),
        path(r'<int:region_id>/records', RegionRecordListView.as_view(), name='region-record-list'),
        path(r'<int:region_id>/records/sector_values', RegionRecordValueEvolutionBySectorView.as_view(), name='region-records-sector-values'),
        path(r'<int:region_id>/records/values', RegionRecordValueByGenericView.as_view(), name='region-records-grouped-values'),
        path(r'<int:region_id>/records/by_status', RegionRecordNumberByStatusYearView.as_view(), name='region-records-bystatus-list')
]