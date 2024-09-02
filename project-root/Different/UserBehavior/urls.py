from django.urls import path
from .views import MouseMoveCreateView, KeyPressCreateView, ClickCreateView, predict_view
import sys
print(sys.path)

urlpatterns = [
    path('api/mouse_moves/', MouseMoveCreateView.as_view(), name='mouse_moves'),
    path('api/key_presses/', KeyPressCreateView.as_view(), name='key_presses'),
    path('api/clicks/', ClickCreateView.as_view(), name='clicks'),
    path('predict/', predict_view, name='predict'),
]