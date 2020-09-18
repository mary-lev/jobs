from django.db.models import Count
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponseNotFound, HttpResponseServerError
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, CreateView, UpdateView
from django.views.generic.detail import DetailView

from .models import Vacancy, Company, Specialty, Application, Resume
from .forms import LoginForm, RegisterForm, VacancySend, CompanyForm, VacancyForm


def custom_handler404(request, exception):
    return HttpResponseNotFound('Ничего не нашлось.')


def custom_handler500(request):
    return HttpResponseServerError('В базе ничего нет.')


def index(request):
    specialties = Specialty.objects.all()
    companies = Company.objects.annotate(count=Count('vacancies'))
    return render(request, 'index.html', {
        'specialties': specialties, 'companies': companies})


def show_one_vacancy(request, vacancy_id):
    vacancy = Vacancy.objects.get(id=vacancy_id)
    if request.method == 'POST':
        form = VacancySend(request.POST)
        if form.is_valid():
            new_application = Application.objects.create(
                user=request.user,
                vacancy=vacancy,
                written_username=form.cleaned_data['written_username'],
                written_phone=form.cleaned_data['written_phone'],
                written_cover_letter=form.cleaned_data['written_cover_letter'])
            new_application.save()
            return redirect('vacancies:sent', vacancy_id=vacancy.id)
        else:
            ''
    else:
        form = VacancySend()
    return render(request, 'vacancy.html', {
        'vacancy': vacancy,
        'form': form})


def sent_application(request, vacancy_id):
    return render(request, 'sent.html', {'vacancy_id': vacancy_id})


def has_company(request):
    company = Company.objects.filter(owner=request.user).first()
    if company:
        return redirect('vacancies:company-edit', pk=company.id)
    else:
        return redirect('vacancies:company-create')


class MySignupView(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('vacancies:login')
    template_name = 'register.html'


class MyLoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = '/'


class VacancyCreateView(CreateView):
    model = Vacancy
    template_name = 'vacancy-edit.html'
    fields = '__all__'


class VacancyEditView(UpdateView):
    model = Vacancy
    template_name = 'vacancy-edit.html'
    form_class = VacancyForm


class MyVacancyListView(ListView):
    model = Vacancy
    template_name = 'vacancy-list.html'

    def get_queryset(self):
        vacancies = super().get_queryset()
        vacancies = Vacancy.objects.filter(company__owner=self.request.user.id)
        return vacancies


class CompanyCreateView(CreateView):
    model = Company
    template_name = 'company-edit.html'
    fields = '__all__'


class CompanyEditView(UpdateView):
    model = Company
    template_name = 'company-edit.html'
    form_class = CompanyForm

    def get_success_url(self, **kwargs):
        return reverse_lazy('vacancies:company-edit', args=(self.object.id,))


class CompanyView(DetailView):
    model = Company
    template_name = 'company.html'


class ResumeCreateView(CreateView):
    model = Resume
    template_name = 'resume-edit.html'
    fields = '__all__'


class VacancyListView(ListView):
    model = Vacancy
    template_name = 'vacancies.html'


class VacancyCatListView(ListView):
    model = Vacancy
    template_name = 'vacancies.html'

    def get_queryset(self):
        specialty = Specialty.objects.get(code=self.kwargs['category']).id
        return Vacancy.objects.filter(specialty=specialty)
