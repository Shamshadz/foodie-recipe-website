from django.urls import path
from articles import views

urlpatterns = [
    path('article/',views.article_view,name='article_view'),
]
