from django.urls import path

from . import views

app_name = 'vacancies'

handler404 = views.custom_handler404
handler500 = views.custom_handler500

urlpatterns = [
    path('', views.index, name='index'),
    path('vacancies', views.VacancyListView.as_view(), name='vacancies'),
    path('vacancies/<int:pk>/', views.VacancyView.as_view(), name='vacancy'),
    path('vacancies/cat/<str:category>/',
         views.VacancyCatListView.as_view(),
         name='vacancies_cat'),
    path('companies/<int:pk>/', views.CompanyView.as_view(), name='company'),
]
