from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<int:id>/', views.get_category, name='category'),
]
