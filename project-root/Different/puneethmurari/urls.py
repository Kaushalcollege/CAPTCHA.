from django.urls import path
from . import views

urlpatterns = [
    path('predict/', views.predict_view, name='predict'),  # Pass the view function, not call it
    path('', views.home, name='home'),  # If you have a home view
]
