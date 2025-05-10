from django import forms
from django.core.exceptions import ValidationError
class PredictForm(forms.Form):
    student_id = forms.IntegerField(label="Student ID")
    study_hours = forms.IntegerField(label="Study Hours")
    exam_score = forms.IntegerField(label="Previous Exam Score")

class LoginForm(forms.Form):
    user_name = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    user_name = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    confirm_password = forms.CharField(label="Re-type Password", widget=forms.PasswordInput)
    student_id = forms.IntegerField(label="Student ID")

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise ValidationError("Passwords do not match.")

        return cleaned_data


    
