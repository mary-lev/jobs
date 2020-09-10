from django.urls import path
from . import views


urlpatterns = [
	path('', views.index, name='index'),
    path('vacancies', views.list_vacancies, name='vacancies'),
    path('vacancy/<int:vacancy>/', views.one_vacancy, name='vacancy'),
    path('company', views.company, name='company'),
	]