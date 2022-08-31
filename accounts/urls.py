from accounts import views
from django.urls import path,include

urlpatterns = [
    path('',views.home_view,name="home_view"),
    path('recipe/',views.recipe_page_view,name="recipe_page_view"),
]
