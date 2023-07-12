from django.shortcuts import render
from podcast.models import Podcast, Like
from blog.models import Article


def index(request):
    articles = Article.objects.all()
    podcasts = Podcast.objects.all()
    likes = Like.objects.all()
    context = {
        'articles': articles,
        'podcasts': podcasts,
        'likes': likes
    }

    return render(request, 'about.html', context)
