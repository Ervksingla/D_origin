from django.urls import path
from .views import ContentView, ContentDetailView

urlpatterns = [
    path('', ContentView.as_view(), name='content-list'),
    path('<int:pk>/', ContentDetailView.as_view(), name='content-detail'),
]