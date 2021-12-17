from django.urls import path

from .views import PublishedReleaseView, RecordByTarget, RecordItemList, RecordStageList, InProgressRecordList, DoneRecordList

buyer_urlpatterns = [
    path(r'<int:buyer_id>/records/in_progress/', InProgressRecordList.as_view(), name='buyer-records-inprogress'),
    path(r'<int:buyer_id>/records/done/', DoneRecordList.as_view(), name='buyer-records-done'),
]

record_urlpatterns = [
    path(r'<int:record_id>/items', RecordItemList.as_view(), name='record-item-list'),
    path(r'<int:record_id>/stages', RecordStageList.as_view(), name='record-stage-list'),
    path(r'target/<str:target_name>', RecordByTarget.as_view(), name='record-by-target'),
]

release_urlpatterns = [
    path(r'published/<int:pk>', PublishedReleaseView.as_view(), name='published-release-detail')
]
