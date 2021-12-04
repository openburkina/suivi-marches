from django.urls import path

from .views import TenderViews, TenderByAdress
tender_list = TenderViews.as_view({'get': 'list'})
tender_detail = TenderViews.as_view({'get': 'retrieve'})

urlpatterns = [
        path(r'', tender_list, name='tender-list'),
        path(r'<int:pk>', tender_detail, name='tender-detail'),
        path(r'buyer/<int:buyer_id>', TenderByAdress.as_view()),
]
