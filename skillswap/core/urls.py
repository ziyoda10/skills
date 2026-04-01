# core/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Apps
    path('api/auth/', include('users.urls')),
    path('api/match/', include('match.urls')),  
    path('api/chat/', include('chat.urls')),

    # Keyinroq qo'shish uchun
    # path('api/skills/', include('skills.urls')),
    # path('api/sessions/', include('sessions.urls')),
    # path('api/chat/', include('chat.urls')),
    # path('api/reviews/', include('reviews.urls')),
]