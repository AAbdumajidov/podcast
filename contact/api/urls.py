from django.urls import path
from .views import ContactListCreateAPIVIew, SubscribeListCreateAPIView


urlpatterns = [
    path('contact/list-create/', ContactListCreateAPIVIew.as_view()),
    path('subscribe/list-create/', SubscribeListCreateAPIView.as_view()),
]