from django.urls import path

from .views import (
    BuyerList,
    BuyerRecordByStatus,
    BuyerRecordList,
    BuyerRecordSectorValues,
    BuyerRecordValuesGrouped,
    BuyerTotalRecordView,
    BuyerTransactionList,
    DoneRecordList,
    InProgressRecordList,
    PublishedReleaseView,
    RecordItemList,
    RecordStageList,
    SumRecord,
    BuyerTotalRecord,
    RecordNumberByStatusYearView,
    RecordValueEvolutionBySectorView,
    RecordValueByGenericView,
    AllRecordValueGroupByRegion,
    RecordList,
    RecordDetail,
    RecordTransactionList
)

buyer_urlpatterns = [
    path(r'', BuyerList.as_view(), name='buyer-list'),
    path(r'<int:buyer_id>/records/', BuyerRecordList.as_view(), name='buyer-records-list'),
    path(r'<int:buyer_id>/records/sector_values', BuyerRecordSectorValues.as_view(), name='buyer-records-sector-values'),
    path(r'<int:buyer_id>/records/values', BuyerRecordValuesGrouped.as_view(), name='buyer-records-grouped-values'),
    path(r'<int:buyer_id>/records/by_status', BuyerRecordByStatus.as_view(), name='buyer-records-bystatus-list'),
    path(r'<int:buyer_id>/records/in_progress/', InProgressRecordList.as_view(), name='buyer-records-inprogress'),
    path(r'<int:buyer_id>/records/done/', DoneRecordList.as_view(), name='buyer-records-done'),
    path(r'<int:buyer_id>/records/total/', BuyerTotalRecordView.as_view(), name='buyer-records-total'),
    path(r'<int:buyer_id>/transactions/', BuyerTransactionList.as_view(), name='buyer-transactions-list'),
    path(r'<int:buyer_id>/total/', BuyerTotalRecord.as_view(), name='buyer-transactions-list'),

]

record_urlpatterns = [
    path(r'', RecordList.as_view(), name='record-list'),
    path(r'<int:record_id>', RecordDetail.as_view(), name='record-detail'),
    path(r'<int:record_id>/items', RecordItemList.as_view(), name='record-item-list'),
    path(r'<int:record_id>/stages', RecordStageList.as_view(), name='record-stage-list'),
    path(r'amount_value', SumRecord.as_view(), name='record-count-all'),
    path(r'by_status', RecordNumberByStatusYearView.as_view(), name='record-count-all'),
    path(r'sector_values', RecordValueEvolutionBySectorView.as_view(), name='record-count-all'),
    path(r'values', RecordValueByGenericView.as_view(), name='record-count-all'),
    path(r'amountvalue', AllRecordValueGroupByRegion.as_view(), name='record-count-region'),
    path(r'<int:record_id>/transactions/', RecordTransactionList.as_view(), name='record-transactions-list'),

]
release_urlpatterns = [
    path(r'published/<int:pk>', PublishedReleaseView.as_view(), name='published-release-detail')
]
