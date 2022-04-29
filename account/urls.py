from django.urls import path

from account.views import MeView

urlpatterns = [
    path('me/', MeView.as_view())
]
