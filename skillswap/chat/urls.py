from django.urls import path
from .views import SessionMessagesView

urlpatterns = [
    path('session/<int:session_id>/messages/', SessionMessagesView.as_view(), name='session-messages'),
]
