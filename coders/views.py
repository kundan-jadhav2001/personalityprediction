from django.shortcuts import render
import joblib ,os
from django.conf import settings

# Create your views here.
def home(request):
    return render(request, 'home.html')

def test(request):
    return render(request, 'test.html')

def result(request):
    if request.method == "POST":
        name = request.POST['name']
        age = int(request.POST['age'])
        gender = request.POST['gender']
        if gender.lower() == 'male':
            gender = 0
        else:
            gender = 1

        openness = int(request.POST['openness'])
        neuroticism = int(request.POST['neuroticism'])
        conscientiousness = int(request.POST['conscientiousness'])
        agreeableness = int(request.POST['agreeableness'])
        extraversion = int(request.POST['extraversion'])

        with open(os.path.join(settings.BASE_DIR, 'coders\\train_model.pkl'),'rb') as f:
            model = joblib.load(f)
            pred = model.predict([[gender,age,openness,neuroticism,conscientiousness,agreeableness,extraversion]])

    return render(request, 'result.html', {'name':name,'pred':pred[0]})