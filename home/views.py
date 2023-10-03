from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    return render(request, 'home/home.html')
    # return HttpResponse("this is home page")


def contact(request):
    return render(request, 'home/contact.html')


def about(request):
    return render(request, 'home/about.html')


def search(request):
    return render(request, 'home/search.html')
