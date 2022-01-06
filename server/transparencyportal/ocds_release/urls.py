from django.urls import path

from .views import (
    BuyerList,
    BuyerTotalRecordView,
    DoneRecordList,
    InProgressRecordList,
    PublishedReleaseView,
    RecordItemList,
    RecordStageList,
    SumRecord,
)

buyer_urlpatterns = [
    path(r'', BuyerList.as_view(), name='buyer-list'),
    path(r'<int:buyer_id>/records/in_progress/', InProgressRecordList.as_view(), name='buyer-records-inprogress'),
    path(r'<int:buyer_id>/records/done/', DoneRecordList.as_view(), name='buyer-records-done'),
    path(r'<int:buyer_id>/records/total/', BuyerTotalRecordView.as_view(), name='buyer-records-total'),
]

record_urlpatterns = [
    path(r'<int:record_id>/items', RecordItemList.as_view(), name='record-item-list'),
    path(r'<int:record_id>/stages', RecordStageList.as_view(), name='record-stage-list'),
    path(r'amount_value', SumRecord.as_view(), name='record-count-all'),
]

release_urlpatterns = [
    path(r'published/<int:pk>', PublishedReleaseView.as_view(), name='published-release-detail')
]
