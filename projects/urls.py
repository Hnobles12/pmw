from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.main),
    path('vue_test', views.vue_test),
]