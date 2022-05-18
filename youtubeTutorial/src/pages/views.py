from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "home.html", {}) # string of HTML code

def contact_view(request, *args, **kargs):
    return render(request, "contact.html", {})

def about_view(request, *args, **kargs):
    my_context = {
        "my_text": "This is about us",
        "my_number": 123,
        "my_list": [123, 4242, 12313]
    }
    
    return render(request, "about.html", my_context)

def social_view(request, *args, **kargs):
    return HttpResponse("<h1> Social Page </h1>")
