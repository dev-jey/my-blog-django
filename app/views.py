from django.shortcuts import render
from .models import Article, User, Category


def get_all_categories():
    return Category.objects.all()

def get_user():
    return User.objects.get(is_superuser=True)

def get_all_articles():
    return Article.objects.all()

def index(request):
    cover_articles = get_all_articles()[:3]
    featured_articles = get_all_articles()[:4]
    popular_articles = get_all_articles()[:4][::-1]
    recent_articles = get_all_articles()[:4]
    latest_article = get_all_articles()[0]
    categories = get_all_categories()
    other_articles = get_all_articles()[:4]
    context = {
        'cover_articles': cover_articles,
        'featured_articles': featured_articles,
        'popular_articles': popular_articles,
        'recent_articles': recent_articles,
        'latest_article':latest_article,
        'categories': categories,
        'other_articles':other_articles,
        'user': get_user()
    }
    return render(request, 'blog/index.html', context)


def get_category(request, id):
    category = Category.objects.get(id=id)
    articles = Article.objects.filter(category=category)
    context = {
        'category': category,
        'categories': get_all_categories(),
        'category_articles': articles,
        'user': get_user(),
        'featured_articles':get_all_articles()[:4]
    }
    return render(request, 'blog/category.html', context)
