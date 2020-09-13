from django.db.models import Count
from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseServerError
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .models import Vacancy, Company, Specialty


def custom_handler404(request, exception):
    return HttpResponseNotFound('Ничего не нашлось.')


def custom_handler500(request):
    return HttpResponseServerError('В базе ничего нет.')


def index(request):
    vacancies = dict()
    specialties = Specialty.objects.values_list('pk', 'code')
    for specialty in specialties:
        vacancies[specialty[1]] = Vacancy.objects.filter(
            specialty=specialty[0]).count()
    companies = Company.objects.annotate(count=Count('vacancies'))
    return render(request, 'index.html', {'vacancies': vacancies, 'companies': companies})


class VacancyView(DetailView):
    model = Vacancy
    template_name = 'vacancy.html'


class CompanyView(DetailView):
    model = Company
    template_name = 'company.html'


class VacancyListView(ListView):
    model = Vacancy
    template_name = 'vacancies.html'


class VacancyCatListView(ListView):
    model = Vacancy
    template_name = 'vacancies.html'

    def get_queryset(self):
        specialty = Specialty.objects.get(code=self.kwargs['category']).id
        return Vacancy.objects.filter(specialty=specialty)
