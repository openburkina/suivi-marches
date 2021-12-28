from django.urls import path

from .views import TenderViews, TenderByAdress, TenderStateAndMount
tender_list = TenderViews.as_view({'get': 'list'})
tender_detail = TenderViews.as_view({'get': 'retrieve'})

urlpatterns = [
        path(r'', tender_list, name='tender-list'),
        path(r'<int:pk>', tender_detail, name='tender-detail'),
        path(r'buyer/<int:buyer_id>/total_by_region', TenderByAdress.as_view(), name='buyer-project-totalbyregion'),
        path(r'year/<year_val>/tender_state', TenderStateAndMount.as_view()),
]
