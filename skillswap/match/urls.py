from django.urls import path
# from .views import AcceptMatchView
from .views import MatchSuggestionView, SendMatchRequestView
from .views import MatchSuggestionView, SendMatchRequestView, AcceptMatchView



urlpatterns = [
    #path("accept/<int:match_id>/", AcceptMatchView.as_view()),
     path('suggestions/', MatchSuggestionView.as_view(), name='match-suggestions'),
    path('send/', SendMatchRequestView.as_view(), name='send-match'),
    path('accept/<int:match_id>/', AcceptMatchView.as_view(), name='accept-match'),
]

from .views import (
    MatchSuggestionView,
    SendMatchRequestView,
    AcceptMatchView
)



