import requests, random
from django.shortcuts import render
from dotenv import load_dotenv
from django.conf import settings
import os

load_dotenv()

API_KEY = os.environ.get('API_KEY')

# Create your views here.

# *********************************************************************************************************
def change_recipe():
    url = "https://random-recipes.p.rapidapi.com/ai-quotes/50"

    headers = {
        "X-RapidAPI-Key":  'API_KEY',
        "X-RapidAPI-Host": "random-recipes.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers).json()
    res = response
    return res
# *********************************************************************************************************

def home_view(request):

    #     0:
    # id:202
    # title:
    # ingredients:
    # instructions:
    # times:
    # image:

    context = {'res' : change_recipe(), 'iterator':range(0,11)}

    return render(request,'home.html', context=context)


# recipe page view *******************************************************************************************
def recipe_page_view(request):

    return render(request, 'recipe_page.html')


# article view page ******************************************************************************************
def article_view(request):
    
    context = {'res' : change_recipe()[1]}

    return render(request,'article_page.html',context=context)