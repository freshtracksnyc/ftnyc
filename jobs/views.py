from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'jobs/home.html')

def about(request):
    return render(request, 'jobs/about.html')

def map(request):
    return render(request, 'jobs/map.html')