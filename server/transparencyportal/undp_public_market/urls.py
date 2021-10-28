from django.urls import path, include
from rest_framework import routers

from .views import ViewsetOffer, ViewsetLessor, ViewsetOfferDate, ViewsetDisbursment
router = routers.DefaultRouter()

router.register('api/offer', ViewsetOffer, 'offer')
router.register('api/lessor', ViewsetLessor, 'lessor')
router.register('api/offerdate', ViewsetOfferDate, 'offerdate')
router.register('api/disbursment', ViewsetDisbursment, 'disbursment')

urlpatterns = [
    path('', include(router.urls))
]