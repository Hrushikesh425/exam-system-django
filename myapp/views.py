from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from myapp.models import Contact


# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def maths(request):
    return render(request, 'maths.html')

def class11(request):
    return render(request, 'class11.html')

def class12(request):
    return render(request, 'class12.html')

def class11sets(request):
    return render(request, 'class11sets.html')

def class11physicalworld(request):
    return render(request, 'class11physicalworld.html')

def class12relations(request):
    return render(request, 'class12relations.html')

def class12electricchargesandfield(request):
    return render(request, 'class12electricchargesandfield.html')

def physics(request):
    return render(request, 'physics.html')

def chemistry(request):
    return render(request, 'chemistry.html')

def cs1(request):
    return render(request, 'cs1.html')

def cs2(request):
    return render(request, 'cs2.html')

def it(request):
    return render(request, 'it.html')


def handlesignup(request):
    if request.method == 'POST':
        # Get user parameters
        username = request.POST['username']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

    
        if len(username)  > 10:
            messages.error(request, 'Username must be less than 10 characters')
            return redirect('/index')

        if not username.isalnum():
            messages.error(request, 'Username should contain only alphabets and numbers')
            return redirect('/index')

        if pass1 != pass2:
            messages.error(request, 'Passwords does not match')
            return redirect('/index')


        # Create User
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request, 'Your account has been created succesfully')
        return redirect('/index')
    else:
        return HttpResponse('404 - Not Found')



def handlelogin(request):

    if request.method == "POST":
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']

        user = authenticate(username=loginusername, password=loginpass)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged in")
            return render(request, "index.html")
        
        else:
            messages.error(request, "Invalid crediantials, please try again!")
            return redirect("/index")


    return HttpResponse('404 - Not Found')
    
def handlelogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect("/index")

    return HttpResponse('404 - Not Found')

def user(request):
    return render(request, "user.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, desc=desc)
        contact.save()
        messages.success(request, "Your message has been sent")
        return redirect("/index")

    return render(request, 'contact.html')


