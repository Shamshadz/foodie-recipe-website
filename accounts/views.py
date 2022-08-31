import re
from django.shortcuts import render

# Create your views here.
def home_view(request):

    return render(request,'home.html')

def recipe_page_view(request):

    return render(request, 'recipe_page.html')