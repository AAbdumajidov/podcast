from django.urls import path
from .views import index, episodes_list, episode_detail, like, get_ids_list

app_name = 'podcast'

urlpatterns = [
    path('', index, name='index'),
    path('episode_list/', episodes_list, name='list'),
    path('episode_detail/<int:pk>/', episode_detail, name='detail'),
    path('like/', like, name='like'),
    path('ids_list/', get_ids_list, name='get_ids_list')
]