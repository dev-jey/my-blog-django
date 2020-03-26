from django.shortcuts import render
from .models import Article, User, Category


def index(request):
    cover_articles = Article.objects.all()[:3]
    featured_articles = Article.objects.all()[:4]
    popular_articles = Article.objects.all()[:4][::-1]
    recent_articles = Article.objects.all()[:4]
    latest_article = Article.objects.all()[0]
    categories = Category.objects.all()
    other_articles = Article.objects.all()[:4]
    user = User.objects.get(is_superuser=True)
    context = {
        'cover_articles': cover_articles,
        'featured_articles': featured_articles,
        'popular_articles': popular_articles,
        'recent_articles': recent_articles,
        'latest_article':latest_article,
        'categories': categories,
        'other_articles':other_articles,
        'user': user
    }
    return render(request, 'blog/index.html', context)
