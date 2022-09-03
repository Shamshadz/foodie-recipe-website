from django.urls import path, include
from accounts import views
from articles.views import home_view

urlpatterns = [
    path('',views.home_view,name="home_view"),
    path('signup',views.signup_view),
    path('login',views.login_view),
    path('logout',views.logout_view),
]
