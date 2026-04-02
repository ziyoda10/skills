from django.urls import path
from .views import GiveRatingView, UserRatingView

urlpatterns = [
    path('give/', GiveRatingView.as_view()),
    path('user/<int:user_id>/', UserRatingView.as_view()),
]