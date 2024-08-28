from django.urls import path
from .views import MouseMoveCreateView, KeyPressCreateView, ClickCreateView

urlpatterns = [
    path('api/mouse_moves/', MouseMoveCreateView.as_view(), name='mouse_move_create'),
    path('api/key_presses/', KeyPressCreateView.as_view(), name='key_press_create'),
    path('api/clicks/', ClickCreateView.as_view(), name='click_create'),
]
