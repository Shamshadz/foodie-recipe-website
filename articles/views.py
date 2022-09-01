import requests, random
from django.shortcuts import render

# Create your views here.

# *********************************************************************************************************
def change_recipe():
    url = "https://random-recipes.p.rapidapi.com/ai-quotes/50"

    headers = {
        "X-RapidAPI-Key": "94ef74103emsha7e58d2e3a63508p167a62jsn8cd9ca167ba0",
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