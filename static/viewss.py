# from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Tag, Episode, Like
from .forms import CommentForm
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.decorators.csrf import csrf_exempt


def index(request):
    categories = Category.objects.all()
    tags = Tag.objects.all()
    articles = Episode.objects.order_by('-id')[:3]
    ctx = {
        'categories': categories,
        'tags': tags,
        'articles': articles
    }

    return render(request, 'mypodcast/index.html', ctx)


def episode(request, pk):
    article = get_object_or_404(Episode, id=pk)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    form = CommentForm()
    if request.method == "POST":
        if not request.user.is_authenticated:
            form = CommentForm(data=request.POST)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.article_id = article.id
                obj.save()
                return redirect('.')
        form = CommentForm(data=request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author_id = request.user.singer.id
            obj.name = request.user.singer.full_name
            obj.article_id = article.id
            obj.save()
            return redirect('.')
    ctx = {
        'object': article,
        'categories': categories,
        'tags': tags,
        'form': form,
    }
    return render(request, 'mypodcast/episode.html', ctx)


# def episode(request, pk):
#     # article = get_object_or_404(Article, id=pk)
#     template_name = 'blog/blog_details.html'
#     if pk is not None:
#         blog = get_object_or_404(Article, id=pk)
#     else:
#         blog = None
#     comment_form = CommentForm(request.POST)
#     queryset = Article.objects.filter(is_published="published", blog=pk)
#
#     if request.method == "POST":
#         if comment_form.is_valid():
#                 isinstance = comment_form.save(commit=False)
#                 if request.user.is_authenticated:
#                     isinstance.user = request.user
#                 elif request.user.is_anonymous:  # AnonymousUser code
#                     isinstance.user = None
#                 isinstance.blog = blog
#                 isinstance.save()
#                 messages.add_message(request, messages.INFO, 'Your Comment Pending for admin approval')
#                 return redirect('blog:blog-detail', pk=blog.pk)
#         else:
#             messages.add_message(request, messages.INFO, 'Somethings Wrong. Please try again')
#     else:
#         comment_form = CommentForm()
#
#     context = {
#         "blog": blog,
#         "comment_form": comment_form,
#         "queryset": queryset
#
#     }
#     return render(request, 'mypodcast/episode.html', context)


def login_view(request):

    if not request.user.is_anonymous:
        # messages.info(request, "Siz login qilib bo'lgansiz")
        return redirect('my_podcast:index')
    form = AuthenticationForm(request)
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_path = request.GET.get('next')
            # messages.success(request, "Muvaffaqiyatli login qildingiz")
            if next_path:
                return redirect(next_path)
            return redirect('my_podcast:index')
        return render(request, 'login.html')
    cxt = {
        'form': form
    }
    return render(request, 'login.html', cxt)


def logout_view(request):
    if not request.user.is_authenticated:
        return redirect('my_podcast:login')
    if request.method == 'POST':
        logout(request)
        return redirect('my_podcast:login')

    return render(request, 'logout.html')


def register_view(request):
    if request.user.is_authenticated:
        return redirect('my_podcast:index')
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        # messages.success(request, "Muvofaqiyatli ro'yhatdan o'tdingiz!")
        return redirect('my_podcast:login')
    context = {
        'form': form
    }
    return render(request, 'register.html', context)


@csrf_exempt
def like(request):
    print('like is working!')
    if not request.user.is_authenticated:
        return JsonResponse({"detail": "You should authorize!"}, status=401)
    if request.method == "POST":
        music_id = int(request.POST.get('music_id'))
        user_id = request.user.singer.id
        likes = Like.objects.values_list('music_id', 'author_id')
        if (music_id, user_id) in likes:
            Like.objects.get(music_id=music_id, author_id=user_id).delete()
            return JsonResponse({"detail": "Un-liked"})
        Like.objects.create(music_id=music_id, author_id=user_id)
        return JsonResponse({"detail": "Liked"})
    return JsonResponse({"detail": "Method not allowed!"})
