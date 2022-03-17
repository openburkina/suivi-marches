from django.urls import path

from .views import RegionListView, RegionRecordListView, RegionRecordNumberByStatusYearView, RegionRecordValueByGenericView, RegionRecordValueEvolutionBySectorView

urlpatterns = [
]

region_urlpatterns = [
        path(r'', RegionListView.as_view(), name='region-list'),
        path(r'records', RegionRecordListView.as_view(), name='region-record-list'),
        path(r'records/sector_values', RegionRecordValueEvolutionBySectorView.as_view(), name='region-records-sector-values'),
        path(r'records/values', RegionRecordValueByGenericView.as_view(), name='region-records-grouped-values'),
        path(r'records/by_status', RegionRecordNumberByStatusYearView.as_view(), name='region-records-bystatus-list')
]