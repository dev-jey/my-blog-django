import os
from django.shortcuts import render
from .models import Article, User, Category
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist


def get_all_categories():
    return Category.objects.all()


def get_user():
    return User.objects.get(is_superuser=True)


def get_all_articles():
    return Article.objects.all()


def index(request):
    try:
        cover_articles = get_all_articles()[:3]
        featured_articles = get_all_articles()[:4]
        popular_articles = get_all_articles()[:4][::-1]
        recent_articles = get_all_articles()[:4]
        latest_article = get_all_articles()[0]
        other_articles = get_all_articles()[:4]
        context = {
            'cover_articles': cover_articles,
            'featured_articles': featured_articles,
            'popular_articles': popular_articles,
            'recent_articles': recent_articles,
            'latest_article': latest_article,
            'categories': get_all_categories(),
            'other_articles': other_articles,
            'user': get_user()
        }
        for cat in get_all_categories():
            print(cat.image)
        return render(request, 'blog/index.html', context)
    except Exception as e:
        raise http500("No articles yet")


def get_category(request, id):
    category = Category.objects.get(id=id)
    articles = Article.objects.filter(category=category)
    context = {
        'category': category,
        'categories': get_all_categories(),
        'category_articles': articles,
        'user': get_user(),
        'featured_articles': get_all_articles()[:4]
    }
    return render(request, 'blog/category.html', context)


def view_article(request, slug):
    article = Article.objects.get(slug=slug)
    context = {
        'article': article,
        'categories': get_all_categories(),
        'user': get_user(),
        'featured_articles': get_all_articles()[:4]
    }
    return render(request, 'blog/article.html', context)


def view_about(request):
    context = {
        'categories': get_all_categories(),
        'user': get_user(),
        'featured_articles': get_all_articles()[:4]
    }
    return render(request, 'blog/about.html', context)


##
# Handle server Errors
def error404(request, exception):
    context = {
        'categories': get_all_categories(),
        'user': get_user(),
        'featured_articles': get_all_articles()[:4]
    }
    response = render(request, "blog/404.html", context)
    response.status_code = 404
    return response

def error500(request):
    context = {
    }
    response = render(request, "blog/500.html", context)
    response.status_code = 500
    return response