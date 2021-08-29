from django.db.models import Prefetch
from django.shortcuts import render

from articles.models import Article, Membership


def articles_list(request):
    tags = Membership.objects.select_related('tag')
    prefetch = Prefetch('tags', queryset=tags.only('tag_id', 'is_tag_primary').order_by('-is_tag_primary'))
    articles = Article.objects.prefetch_related(prefetch)

    template = 'articles/news.html'
    context = {
        'object_list': articles
    }

    return render(request, template, context)
