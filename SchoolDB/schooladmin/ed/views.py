from typing import Any, Dict
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Teacher, Student, School
from django.views.generic import TemplateView, ListView, CreateView, DeleteView, UpdateView, DetailView
from .forms import SchoolForm, TeacherForm, StudentForm
from django.urls import reverse




class TemplateView(TemplateView):
    template_name = "base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['insert'] = 'School admin'
        context['insert1'] = 'Teacher-Student meeting'
        return context
# def HomeView(request):
#     context = {'insert' : 'School admin', 'insert1' : 'Student-Teacher meeting'}
#     return render(request, 'home.html/', context)

class SchoolListView(ListView):
    model = School
    context_object_name = "school_list"
    template_name = "school_list.html"

    def get_context_data(self, **kwargs):  
        context = super().get_context_data(**kwargs)
        context["state"] = School.objects.values_list('state', flat = True).distinct
        return context

class CreateSchoolView(CreateView):
    model = School
    form_class = SchoolForm
    template_name = "school_create.html"
    success_url = "/list/"

class UpdateSchoolView(UpdateView):
    model = School
    form_class = SchoolForm
    template_name = "update_school.html"
    success_url = "/list/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["school_name"] = self.object.school_name
        return context

class DeleteSchoolView(DeleteView):
    def post(self, request, pk):
        school = get_object_or_404(School, pk=pk)
        school.delete()
        return redirect('school_list')

class CreateTeacherView(CreateView):
    model = Teacher
    form_class = TeacherForm
    template_name = "teacher_create.html"
    success_url = "/list/"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['form_teacher'] = self.get_form()
    #     return context

class CreateStudentView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = "student_create.html"
    success_url = "/list/"

class SchoolDetailView(DetailView):
    model = School
    template_name = 'details.html'
    context_object_name = 'school'

  