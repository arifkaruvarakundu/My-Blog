from django.shortcuts import render

# Create your views here.
from django.views import View
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from blog.models import Post

class IndexView(View):
    def get(self, request):
        top_posts = Post.objects.order_by('-created_on')[:4]
        context = {'top_posts': top_posts}
        return render(request, 'home/index.html', context)


class SignupView(View):
    def post(self, request):
        if request.method == "POST":
            # get the post parameters
            fname = request.POST['fname']
            lname = request.POST['lname']
            username = request.POST['username']
            email = request.POST['email']
            pass1 = request.POST['pass1']
            pass2 = request.POST['pass2']

            # check input
            if len(username) > 10:
                messages.error(request, "Username should be under 10 characters")
                return redirect('/')
            if not username.isalnum():
                messages.error(request, "Username should be characters and numbers")
                return redirect('/')
            if pass1 != pass2:
                messages.error(request, "Passwords didn't match")
                return redirect('/')

            # create user
            myuser = User.objects.create_user(username, email, pass1)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()
            messages.success(request, "Created account in myblogs successfully!")
            return redirect("/")
        else:
            return HttpResponse("404 Not Found")

class LoginView(View):
    def post(self, request):
        if request.method == "POST":
            loginusername = request.POST['loginusername']
            loginpassword = request.POST['loginpassword']
            user = authenticate(username=loginusername, password=loginpassword)
            if user is not None:
                login(request, user)
                messages.success(request, "Successfully Logged In")
                return redirect('/')
            else:
                messages.error(request, "Invalid Credentials, Please Try Again")
                return redirect("/")
        return HttpResponse('404 Not Found')

class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'Logged Out Done')
        return redirect('/')
 