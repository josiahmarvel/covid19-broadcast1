from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('speeches/', views.SpeechListView.as_view(), name='speeches'),
    path('speakers/', views.SpeakerListView.as_view(), name='speakers'),
    path('speech/<int:pk>', views.SpeechDetailView.as_view(), name='speech-detail'),
    path('speaker/<int:pk>', views.SpeakerDetailView.as_view(), name='speaker-detail'),
]