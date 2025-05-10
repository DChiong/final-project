from django.shortcuts import render, redirect
from .models import StudentRecord
from .forms import PredictForm, LoginForm,RegisterForm
import joblib
import os


def prediction_history(request):
    # Fetch all records from the StudentRecord model
    records = StudentRecord.objects.all()

    # Pass records to the template
    return render(request, 'history.html', {'records': records})




# Load model once (global variable)
model_path = os.path.join(os.path.dirname(__file__), 'models', 'model.pkl')
model = joblib.load(model_path)

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['user_name']
            password = form.cleaned_data['password']
            return redirect('home') 
            # You can add actual authentication here
            if user_name == 'admin' and password == 'admin':
                return redirect('predict')  # This redirects to the 'home' URL pattern
    else:
        form = LoginForm()

    return render(request, 'index.html', {"form": form})


# Create your views here.
def home_view(request):

    return render(request, 'home.html')



def predict_view(request):
    prediction = None
   
    if request.method == 'POST':
        form = PredictForm(request.POST)
        if form.is_valid():
            student_id = form.cleaned_data['student_id']
            study_hours = form.cleaned_data['study_hours']
            exam_score = form.cleaned_data['exam_score']
            pred = model.predict([[study_hours, exam_score]])[0]
            prediction = "PASS" if pred == 1 else "FAIL"
            # Save to StudentRecord
            StudentRecord.objects.create(
                student_id=student_id,
                study_hours=study_hours,
                previous_exam_score=exam_score,
                pass_fail=bool(pred)
            )
    else:
        form = PredictForm()
    records = StudentRecord.objects.all()
   
    return render(request, 'predict.html', {'form': form, 'prediction': prediction, "records": records,})


def dashboard_view(request):

    records = StudentRecord.objects.all()
   
    return render(request, 'dashboard.html', {"records": records})

def registration_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # handle success (e.g., save user, redirect)
            pass
    else:
        form = RegisterForm()
    
    return render(request, 'registration.html', {"form": form})
