
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Teacher, Student, School
from django.views.generic import TemplateView, ListView, CreateView, DeleteView, UpdateView, DetailView
from .forms import SchoolForm, TeacherForm, StudentForm
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin




class TemplateView(TemplateView):
    template_name = "base.html"

class AboutView(TemplateView):
    template_name = "about.html"

class ContactView(TemplateView):
    template_name = "contact.html"
    
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

class CreateSchoolView(CreateView,LoginRequiredMixin):
    model = School
    form_class = SchoolForm
    template_name = "school_create.html"
    success_url = "/list/"

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponse("Warning: Error 405 - You do not have permission to access this page.")
        return super().dispatch(request, *args, **kwargs)

class UpdateSchoolView(UpdateView, LoginRequiredMixin):
    model = School
    form_class = SchoolForm
    template_name = "update_school.html"
    success_url = "/list/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["school_name"] = self.object.school_name
        return context
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponse("Warning: Error 405 - You do not have permission to access this page.")
        return super().dispatch(request, *args, **kwargs)

class DeleteSchoolView(DeleteView, LoginRequiredMixin):
    def post(self, request, pk):
        school = get_object_or_404(School, pk=pk)
        school.delete()
        return redirect('school_list')
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponse("Warning: Error 405 - You do not have permission to access this page.")
        return super().dispatch(request, *args, **kwargs)

class CreateTeacherView(CreateView, LoginRequiredMixin):
    model = Teacher
    form_class = TeacherForm
    template_name = "teacher_create.html"
    success_url = "/list/"

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponse("Warning: Error 405 - You do not have permission to access this page.")
        return super().dispatch(request, *args, **kwargs)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['form_teacher'] = self.get_form()
    #     return context

class CreateStudentView(CreateView, LoginRequiredMixin):
    model = Student
    form_class = StudentForm
    template_name = "student_create.html"
    success_url = "/list/"

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponse("Warning: Error 405 - You do not have permission to access this page.")
        return super().dispatch(request, *args, **kwargs)

class SchoolDetailView(DetailView):
    model = School
    template_name = 'details.html'
    context_object_name = 'school'

  