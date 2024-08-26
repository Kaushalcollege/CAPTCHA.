from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # This maps the root URL to the index view
    path('api/mouse_moves/', views.mouse_moves, name='mouse_moves'),
    path('api/key_presses/', views.key_presses, name='key_presses'),
    path('api/clicks/', views.clicks, name='clicks'),
]
