from django.urls import path
from rest_framework.authtoken import views
from .views import MyProfile

urlpatterns = [
    path('login/', views.obtain_auth_token),
    path('my/profile/', MyProfile.as_view()),

]


