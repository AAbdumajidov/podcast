from django.urls import path
from .views import (
    CategoryListCreateView,
    TagListCreateView,
    SeasonListCreateView,
)


urlpatterns = [
    path('category/list-create/', CategoryListCreateView.as_view()),
    path('tag/list-create/', TagListCreateView.as_view()),
    path('season/list-create/', SeasonListCreateView.as_view()),
]