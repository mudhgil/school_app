from .models import Student, School, Teacher
from django import forms

class SchoolForm(forms.ModelForm):
    
    class Meta:
        model = School
        fields = "__all__"


class TeacherForm(forms.ModelForm):

    class Meta():
        model = Teacher
        fields = '__all__'

class StudentForm(forms.ModelForm):

    class Meta():
        model = Student
        fields = '__all__'
