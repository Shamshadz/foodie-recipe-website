from django.urls import path
from articles import views

urlpatterns = [
    path('',views.home_view,name="home_view"),
    path('article/',views.article_view,name='article_view'),
    path('recipe/',views.recipe_page_view,name="recipe_page_view"),
]
