"""
URL configuration for Different project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from UserBehavior import views as user_behavior_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/mouse_moves/', user_behavior_views.MouseMoveCreateView.as_view(), name='mouse_move_create'),
    path('api/key_presses/', user_behavior_views.KeyPressCreateView.as_view(), name='key_press_create'),
    path('api/clicks/', user_behavior_views.ClickCreateView.as_view(), name='click_create'),
    path('', user_behavior_views.home, name='home'),  # Existing home view

    # Include the URLs for the puneethmurari app
    path('predict/', include('puneethmurari.urls')),  # Add this line to include the predict/ URLs
]
