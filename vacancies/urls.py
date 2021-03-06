from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views

app_name = 'vacancies'

handler404 = views.custom_handler404
handler500 = views.custom_handler500

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.MySignupView.as_view(), name='register'),
    path('login', views.MyLoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('companies', views.CompanyListView.as_view(), name='companies'),
    path('vacancies', views.VacancyListView.as_view(), name='vacancies'),
    path('vacancies/<int:vacancy_id>/', views.ApplicationCreateView.as_view(), name='vacancy'),
    path('vacancies/cat/<str:category>/',
         views.VacancyCatListView.as_view(),
         name='vacancies_cat'),
    path('vacancies/<int:vacancy_id>/sent', views.sent_application, name='sent'),
    path('companies/<int:pk>/', views.CompanyView.as_view(), name='company'),
    path('mycompany', views.has_company, name='mycompany'),
    path('myresume', views.has_resume, name='myresume'),
    path('mycompany/company-create', views.CompanyCreateView.as_view(), name='company-create'),
    path('mycompany/company-edit/<int:pk>/', views.CompanyEditView.as_view(), name='company-edit'),
    path('mycompany/vacancies', views.MyVacancyListView.as_view(), name='my_vacancies'),
    path('mycompany/vacancies/<int:pk>/', views.VacancyEditView.as_view(), name='vacancy-edit'),
    path('mycompany/vacancy-create', views.VacancyCreateView.as_view(), name='vacancy-create'),
    path('resume-edit/<int:pk>/', views.ResumeUpdateView.as_view(), name='resume-edit'),
    path('resume-create', views.ResumeCreateView.as_view(), name='resume-create'),
    path('search', views.VacancySearch.as_view(), name='search'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
