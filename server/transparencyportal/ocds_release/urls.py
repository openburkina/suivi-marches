from django.urls import path

from .views import PublishedReleaseView, RecordItemList, RecordStageList, InProgressRecordList, DoneRecordList

buyer_urlpatterns = [
    path(r'<int:buyer_id>/records/in_progress/', InProgressRecordList.as_view()),
    path(r'<int:buyer_id>/records/done/', DoneRecordList.as_view()),
]

record_urlpatterns = [
    path(r'<int:record_id>/items', RecordItemList.as_view()),
    path(r'<int:record_id>/stages', RecordStageList.as_view()),
]

release_urlpatterns = [
    path(r'published/<int:pk>', PublishedReleaseView.as_view(), name='published-release-detail')
]
