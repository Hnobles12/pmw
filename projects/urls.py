from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index),
    path('dashboard', views.dashboard, name='dashboard'),
    path('projects/<int:id>', views.project_view),
    path('vue_test', views.vue_test),
]