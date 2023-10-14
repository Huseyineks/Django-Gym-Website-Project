from django.shortcuts import render

def homepage(request):
    return render(request,'homepage.html')
def about(request):
    return render(request,'about.html')
def features(request):
    return render(request,'features.html')
