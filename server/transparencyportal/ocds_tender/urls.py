from django.urls import path

from .views import TenderViews
tender_list = TenderViews.as_view({'get': 'list'})

urlpatterns = [
        path(r'tender', tender_list, name='tender-list'),

    #path('tender', TenderViews.as_view()),
]
