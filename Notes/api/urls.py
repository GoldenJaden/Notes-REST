from django.urls import path
from .views import NoteViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('notes/', NoteViewSet.as_view({'get': 'list',
                                        'post': 'create'})),
    path('notes/<int:pk>', NoteViewSet.as_view({'get': 'retrieve',
                                                'delete': 'destroy',
                                                'patch': 'partial_update'})),
    
    # Authentication
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]