# core/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    # Auth
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Apps
    path('api/auth/', include('users.urls')),
    path('api/match/', include('match.urls')),  
    path('api/chat/', include('chat.urls')),path('api/reviews/', include('reviews.urls')),
    path('api/auth/', include('users.urls')),


    # Keyinroq qo'shish uchun
    # path('api/skills/', include('skills.urls')),
    # path('api/sessions/', include('sessions.urls')),
    # path('api/chat/', include('chat.urls')),
    # path('api/reviews/', include('reviews.urls')),
]