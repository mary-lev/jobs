from django.urls import path
from . import views


app_name = 'vacancies'

urlpatterns = [
	path('', views.index, name='index'),
    path('vacancies', views.VacancyListView.as_view(), name='vacancies'),
    path('vacancies/<int:pk>/', views.VacancyView.as_view(), name='vacancy'),
    path('vacancies/cat/<str:category>/',
        views.VacancyCatListView.as_view(),
        name='vacancies_cat'),
    path('companies/<int:pk>/', views.CompanyView.as_view(), name='company'),
	]