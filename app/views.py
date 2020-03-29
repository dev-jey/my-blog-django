import os
from django.shortcuts import render
from .models import Article, User, Category
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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
    except ObjectDoesNotExist as e:
        print(e)
        raise ObjectDoesNotExist("No articles yet")


def paginate(item_list, request):
    page_number = request.GET.get('page')
    paginator = Paginator(item_list, 10)
    try:
        items = paginator.get_page(page_number)
    except PageNotAnInteger:
        items = paginator.get_page(1)
    except EmptyPage:
        items = paginator.get_page(paginator.num_pages)
    return items, paginator


def get_category(request, id):
    category = Category.objects.get(id=id)
    article_list = Article.objects.filter(category=category)
    if article_list:
        articles, paginator = paginate(article_list, request)
    context = {
        'category': category,
        'categories': get_all_categories(),
        'category_articles': articles,
        'paginator': paginator,
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


def search_article(request):
    input_ = request.GET.get('search')
    article_list = Article.objects.filter(title__icontains=input_)
    articles, paginator = paginate(article_list, request)
    context = {
        'search': input_,
        'category_articles': articles,
        'categories': get_all_categories(),
        'paginator': paginator,
        'user': get_user(),
        'featured_articles': get_all_articles()[:4]
    }
    if not articles:
        context['no_articles'] = 'No articles found'
    return render(request, 'blog/search.html', context)

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
