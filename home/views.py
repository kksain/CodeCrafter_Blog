from django.shortcuts import render, HttpResponse
from django.contrib import messages
from home.models import Contact
# Create your views here.


def home(request):
    return render(request, 'home/home.html')
    # return HttpResponse("this is home page")


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['phone']
        
        if len(name)<2 or len(email)<5 or len(phone)<10 or len(content)<4 :
            messages.error(request, "Please fill your form correctly!")
        else:
          contact = Contact(name=name, email=email, phone=phone, content=content)    
          contact.save()
          messages.success(request, "Your form has been submit successfully!")
    return render(request, 'home/contact.html')


def about(request):
    return render(request, 'home/about.html')


def search(request):
    return render(request, 'home/search.html')
