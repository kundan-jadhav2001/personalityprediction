from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def test(request):
    return render(request, 'test.html')

def result(request):
    return render(request, 'result.html')