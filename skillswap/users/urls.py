from django.urls import path
from .views import RegisterView, ProfileView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('profile/', ProfileView.as_view()),
    path("register/", RegisterView.as_view(), name="register"),
]
from django.urls import path
from .views import RegisterView # ProfileView so'zini bu yerdan o'chirib tashlang

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    # Agar pastda ProfileView uchun path bo'lsa, uni ham o'chirib turing yoki # bilan yopib qo'ying
]