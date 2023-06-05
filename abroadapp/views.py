from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')

def canada(request):
    return render(request,'canada.html')

def franchise(request):
    return render(request,'franchise.html')

def award(request):
    return render(request,'award.html')

def presencemedia(request):
    return render(request,'presencemedia.html')

def photogallery(request):
    return render(request,'photogallery.html')

def blog(request):
    return render(request,'blog.html')

def branches(request):
    return render(request,'branches.html')

def ielts(request):
    return render(request,'ielts.html')

def migratecanada(request):
    return render(request,'migratecanada.html')

def readmore(request):
    return render(request,'readmore.html')

def seminar(request):
    return render(request,'seminar.html')

def signup(request):
    return render(request,'signup.html')

def register(request):
    return render(request,'register.html')