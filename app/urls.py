from django.urls import path
from . import views


app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<int:id>/', views.get_category, name='category'),
    path('article/<str:slug>/', views.view_article, name='article'),
    path('about/', views.view_about, name='about'),
]
