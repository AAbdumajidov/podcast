from django.urls import path
from .views import (
    CategoryListCreateView,
    TagListCreateView,
    ArticleListCreateAPIView,
    ArticleRUDView
)


urlpatterns = [
    path('category/list-create/', CategoryListCreateView.as_view()),
    path('tag/list-create/', TagListCreateView.as_view()),
    path('article/list-create/', ArticleListCreateAPIView.as_view()),
    path('article/rud/<int:pk>', ArticleRUDView.as_view()),
]