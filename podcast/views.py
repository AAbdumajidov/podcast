from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import CommentForm
from .models import Podcast, Tag, Category, Like, Season
# Create your views here.


def index(request):
    podcasts = Podcast.objects.order_by('-id')
    try:
        user_id = request.user.profile.id
    except:
        user_id = None
    my_liked_music = Like.objects.filter(author_id= user_id).values('music_id')
    my_liked_music_list = [i for i in my_liked_music]

    tags = Tag.objects.all()
    categories = Category.objects.all()
    tag = request.GET.get('tag')
    cat = request.GET.get('cat')
    if tag:
        podcasts = podcasts.filter(tags__title__exact=tag)
    if cat:
        podcasts = podcasts.filter(cat__titlr__exact=cat)
    ctx = {
        'object_list': podcasts,
        'tags': tags,
        'categories': categories,
        'my_liked_musics_list': my_liked_music_list,
        'cat': cat,
        'tag': tag,
    }
    return render(request, 'index.html', ctx)


def episodes_list(request):
    season = Season.objects.all()
    try:
        user_id = request.user.profile.id
    except:
        user_id = None
    my_liked_music = Like.objects.filter(author_id=user_id).values_list('music_id')
    my_liked_music_list = [i[0] for i in my_liked_music]
    podcasts = Podcast.objects.order_by('-id')
    tags = Tag.objects.all()
    categories = Category.objects.all()
    tag = request.GET.get('tag')
    cat = request.GET.get('cat')
    search = request.GET.get('search')

    if tag:
        podcasts = podcasts.filter(tag__title__exact=tag)
    if cat:
        podcasts = podcasts.filter(cat__titlr__exact=cat)
    if search:
        podcasts = podcasts.filter(title__icontains=search)
    page_number = request.GET.get('page', 1)
    paginator = Paginator(podcasts, 2)
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = page_obj.page(3)
    context = {
        'object_list': page_obj,
        'tags': tags,
        'seasons': season,
        'categories': categories,
        "my_liked_music_list": my_liked_music_list
    }
    return render(request, 'episodes.html', context)


def episode_detail(request, pk):
    podcast = get_object_or_404(Podcast, id=pk)
    try:
        user_id = request.user.profile.id
    except:
        user_id = None
    my_liked_music = Like.objects.filter(author_id= user_id).values('music_id')
    my_liked_music_list = [i for i in my_liked_music]

    tags = Tag.objects.all()
    categories = Category.objects.all()
    tag = request.GET.get('tag')
    cat = request.GET.get('cat')
    if tag:
        podcast = podcast.filter(tags__title__exact=tag)
    if cat:
        podcast = podcast.filter(cat__titlr__exact=cat)
    form = CommentForm()
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect(reverse('account:login'))
        form = CommentForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author_id = request.user.profile.id
            obj.podcast_id = podcast.id
            obj.save()
            return redirect('.')

    ctx = {
        'object': podcast,
        'form': form,
        'my_liked_music_list': my_liked_music_list,
        'tags': tags,
        'categories': categories,
        'cat': cat,
        'tag': tag,
    }
    return render(request, 'episode.html', ctx)


def get_ids_list(request):
    musics = Podcast.objects.all().order_by('-id')
    ids_list = [i.id for i in musics]
    return JsonResponse({'ids_list': ids_list})


@csrf_exempt
def like(request):
    if not request.user.is_authenticated:
        return HttpResponse("You should authorize first")
    if request.method == "POST":
        music_id = int(request.POST.get('music_id'))
        user_id = request.user.profile.id
        likes = Like.objects.values_list("music_id", 'author_id')
        if (music_id, user_id) in likes:
            print("salom")
            Like.objects.get(music_id=music_id, author_id=user_id).delete()
            return JsonResponse({"detail": "Un-Liked"})
        Like.objects.create(music_id=music_id, author_id=user_id)
        return JsonResponse({"detail": "Liked"})
    return JsonResponse({"detail": "Method not allowed"}, status=405)













