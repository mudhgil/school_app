
from django.contrib import admin
from django.urls import path
from ed import views 
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path ("", views.HomeView, name = 'home')
    path("admin/", admin.site.urls),
    path ("", views.TemplateView.as_view(), name = 'home'),
    path ("about/", views.AboutView.as_view(), name = 'about'),
    path ("contact/", views.ContactView.as_view(), name = 'contact'),
    path("list/", views.SchoolListView.as_view(), name = 'school_list'),
    path("create/", views.CreateSchoolView.as_view(), name = 'create_school'),
    path("create_teacher/", views.CreateTeacherView.as_view(), name = 'create_teacher'),
    path("create_student/", views.CreateStudentView.as_view(), name = 'create_student'),
    path('update/<int:pk>', views.UpdateSchoolView.as_view(), name = 'update_school'),
    path('delete/<int:pk>', views.DeleteSchoolView.as_view(), name = 'delete_school'),
    path('detail/<int:pk>', views.SchoolDetailView.as_view(), name = 'detail'),
    path('login/',auth_views.LoginView.as_view(),name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page=''), name='logout'),
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
