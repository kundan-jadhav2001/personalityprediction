from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def test(request):
    return render(request, 'test.html')

def result(request):
    if request.method == "POST":
        name = request.POST['name']
        age = request.POST['age']
        gender = request.POST['gender']

        openness = request.POST['openness']
        neuroticism = request.POST['neuroticism']
        conscientiousness = request.POST['conscientiousness']
        agreeableness = request.POST['agreeableness']
        extraversion = request.POST['extraversion']

        
    return render(request, 'result.html')