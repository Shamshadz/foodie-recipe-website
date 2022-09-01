import requests, random
from django.shortcuts import render

# Create your views here.
def home_view(request):

#     0:
# id:202
# title:"Fall-Apart Caramelized Cabbage"
# ingredients:
# instructions:
# times:
# image:"https://cdn.pixabay.com/photo/2019/06/16/01/30/white-4276765_1280.jpg"

    url = "https://random-recipes.p.rapidapi.com/ai-quotes/50"

    headers = {
        "X-RapidAPI-Key": "94ef74103emsha7e58d2e3a63508p167a62jsn8cd9ca167ba0",
        "X-RapidAPI-Host": "random-recipes.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers).json()

    res = random.choice(response)
    context = {'res' : res}

    return render(request,'home.html', context=context)


def recipe_page_view(request):

    return render(request, 'recipe_page.html')

def article_view(request):

    url = "https://random-recipes.p.rapidapi.com/ai-quotes/50"

    headers = {
        "X-RapidAPI-Key": "94ef74103emsha7e58d2e3a63508p167a62jsn8cd9ca167ba0",
        "X-RapidAPI-Host": "random-recipes.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers).json()

    res = random.choice(response)
    context = {'res' : res}

    return render(request,'article_page.html',context=context)