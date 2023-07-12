from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .serializers import CategorySerializer, TagSerializer, ArticleGetSerializer, ArticlePostSerializer
from ..models import Category, Tag, Article
from .permissions import IsOwnerOrReadOnly, IsAdminUserOrReadOnly


class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class ArticleListCreateAPIView(generics.ListCreateAPIView):
    queryset = Article.objects.order_by('-id')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.queryset.GET.get('q')
        if q:
            qs = qs.filter(title__icontains=q)
        return qs

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ArticleGetSerializer
        if self.request.method == 'POST':
            return ArticlePostSerializer
        return Response({"detail": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


class ArticleRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()

    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ArticleGetSerializer
        return ArticlePostSerializer





