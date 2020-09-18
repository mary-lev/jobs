from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

from . import views

app_name = 'vacancies'

handler404 = views.custom_handler404
handler500 = views.custom_handler500

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.MySignupView.as_view(), name='register'),
    path('login', views.MyLoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('vacancies', views.VacancyListView.as_view(), name='vacancies'),
    path('vacancies/<int:vacancy_id>/', views.show_one_vacancy, name='vacancy'),
    path('vacancies/cat/<str:category>/',
         views.VacancyCatListView.as_view(),
         name='vacancies_cat'),
    path('sent/<int:vacancy_id>/', views.sent_application, name='sent'),
    path('companies/<int:pk>/', views.CompanyView.as_view(), name='company'),
    path('mycompany', views.has_company, name='mycompany'),
    path('company-create', views.CompanyCreateView.as_view(), name='company-create'),
    path('company-edit/<int:pk>/', views.CompanyEditView.as_view(), name='company-edit'),
    path('vacancy-list', views.MyVacancyListView.as_view(), name='my_vacancies'),
    path('vacancy-edit/<int:pk>/', views.VacancyEditView.as_view(), name='vacancy_edit'),
    path('vacancy-create', views.VacancyCreateView.as_view(), name='vacancy_create'),
    path('resume-edit', views.ResumeCreateView.as_view, name='resume-edit'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)
