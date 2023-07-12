from django.shortcuts import render, redirect

from podcast.models import Podcast, Tag, Category
from .forms import ContactForm, SubscribeForm


def contact(request):
    form = ContactForm(request.POST or None)
    forma = SubscribeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('contact:index')
    podcasts = Podcast.objects.order_by('-id')
    tags = Tag.objects.all()
    categories = Category.objects.all()
    tag = request.GET.get('tag')
    cat = request.GET.get('cat')
    if tag:
        podcasts = podcasts.filter(tags__title__exact=tag)
    if cat:
        podcasts = podcasts.filter(cat__titlr__exact=cat)
    context = {
        'form': form,
        'forma': forma,
        'object_list': podcasts,
        'tags': tags,
        'categories': categories,
        'cat': cat,
        'tag': tag,
    }
    return render(request, 'contact.html', context)
