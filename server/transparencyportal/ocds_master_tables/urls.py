from django.urls import path

from .views import FacebookPublishView

urlpatterns = [
        path(r'publish', FacebookPublishView.as_view()),
]