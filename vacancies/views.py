from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from .models import Vacancy, Company, Specialty

def index(request):
    specialties = Specialty.objects.all()
    vacancies = Vacancy.objects.all().aggregate('specialty').annotate()
    return render(request, 'index.html', {})


class VacancyView(DetailView):
    model = Vacancy
    template_name = 'vacancy.html'


class CompanyView(DetailView):
    model = Company
    template_name = 'company.html'

    #def get_context_data(self, **kwargs):
    #    return Vacancy.objects.filter(company=self.kwargs['pk'])


class VacancyListView(ListView):
    model = Vacancy
    template_name = 'vacancies.html'


class VacancyCatListView(ListView):
    model = Vacancy
    template_name = 'vacancies.html'

    def get_queryset(self, **kwargs):
        specialty = Specialty.objects.get(code=self.kwargs['category']).id
        return Vacancy.objects.filter(specialty=specialty)
