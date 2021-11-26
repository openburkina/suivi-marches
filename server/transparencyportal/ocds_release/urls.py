from django.urls import path

from .views import RecordStageList, InProgressRecordList, DoneRecordList

urlpatterns = [
    # path(r'buyers/', ),
    # path(r'buyers/<int:buyer_id>/', ),
    # path(r'buyers/<int:buyer_id>/projects', ),
    path(r'records/<int:record_id>/stages', RecordStageList.as_view()),
    path(r'buyers/<int:buyer_id>/records/in_progress/', InProgressRecordList.as_view()),
    path(r'buyers/<int:buyer_id>/records/done/', DoneRecordList.as_view()),
]
