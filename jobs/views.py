from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'jobs/home.html')

def test(request):
    return render(request, 'jobs/test.html')

def about(request):
    return render(request, 'jobs/about.html')