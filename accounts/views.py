from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from articles.views import home_view
from django.contrib.auth import authenticate,login ,logout

# Create your views here.
def signup_view(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']

        myuser = User.objects.create_user(username,email,pass1)

        myuser.save()
        
        messages.success(request, "Your Account is has been created")

        return home_view(request)

    return home_view(request)


def login_view(request):

    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request,user)
            username = user.username
            messages.success(request, "Logged In Sucessfully!!")
            return render(request, "home.html",{'username':username})
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('home_view')

    return home_view(request)

def logout_view(request):
    logout(request)
    messages.success(request, "Logged In Sucessfully!!")
    return redirect('home_view')
