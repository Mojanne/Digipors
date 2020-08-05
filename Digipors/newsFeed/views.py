from django.shortcuts import render



def home(request):
    return render(request, 'newsFeed/home.html')

def humanities(request):
    return render(request, 'newsFeed/humanities.html')

def medical(request):
    return render(request, 'newsFeed/medical.html')

