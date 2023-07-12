from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from .models import Article, Tag, Category


def index(request):
    articles = Article.objects.order_by('id')
    # podcast = Podcast.objects.order_by('-id')
    tags = Tag.objects.all()
    categories = Category.objects.all()
    tag = request.GET.get('tag')
    cat = request.GET.get('cat')
    search = request.GET.get('search')
    if tag:
        articles = articles.filter(tags__title__exact=tag)
    if cat:
        articles = articles.filter(category__title__exact=cat)
    if search:
        articles = articles.filter(search__icontains=search)
    page_number = request.GET.get('page', 1)
    paginator = Paginator(articles, 1)
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = page_obj.page(3)
    ctx = {

        'object_list': page_obj,
        'categories': categories,
        'tags': tags,
        'tag': tag,
        'cat': cat,
    }

    return render(request, 'article_blog.html', ctx)