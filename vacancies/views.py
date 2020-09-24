from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count, Q
from django.http import HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from django.views.generic.detail import DetailView

from .forms import LoginForm, RegisterForm, ApplicationForm, CompanyForm, VacancyForm, ResumeForm
from .models import Vacancy, Company, Specialty, Application, Resume


def custom_handler404(request, exception):
    return HttpResponseNotFound('Ничего не нашлось.')


def custom_handler500(request):
    return HttpResponseServerError('В базе ничего нет.')


def index(request):
    specialties = Specialty.objects.all()
    companies = Company.objects.annotate(count=Count('vacancies'))
    return render(request, 'index.html', {
        'specialties': specialties, 'companies': companies})


def sent_application(request, vacancy_id):
    return render(request, 'sent.html', {'vacancy_id': vacancy_id})


def has_company(request):
    try:
        company = Company.objects.get(owner=request.user.id)
        return redirect('vacancies:company-edit', pk=company.id)
    except ObjectDoesNotExist:
        return render(request, 'company-create.html', {})


def has_resume(request):
    try:
        resume = Resume.objects.get(user=request.user)
        return redirect('vacancies:resume-edit', pk=resume.id)
    except ObjectDoesNotExist:
        return render(request, 'resume-create.html', {})


class ApplicationCreateView(CreateView):
    model = Application
    form_class = ApplicationForm
    template_name = 'vacancy.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.vacancy = Vacancy.objects.get(id=self.kwargs.pop('vacancy_id'))
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        kwargs['vacancy'] = Vacancy.objects.get(id=self.kwargs.pop('vacancy_id'))
        return super().get_context_data(**kwargs)

    def get_success_url(self, **kwargs):
        return reverse_lazy('vacancies:sent', args=(self.object.vacancy_id,))


class MySignupView(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('vacancies:login')
    template_name = 'register.html'


class MyLoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = '/'


class VacancyCreateView(LoginRequiredMixin, CreateView):
    model = Vacancy
    template_name = 'vacancy-edit.html'
    form_class = VacancyForm
    success_url = 'vacancies:vacancy-list'

    def form_valid(self, form):
        form.instance.company = Company.objects.get(owner=self.request.user)
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('vacancies:my_vacancies')


class VacancyEditView(LoginRequiredMixin, UpdateView):
    model = Vacancy
    template_name = 'vacancy-edit.html'
    form_class = VacancyForm

    def form_valid(self, form):
        messages.success(self.request, "some message")
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('vacancies:vacancy-edit', args=(self.object.id,))


class MyVacancyListView(LoginRequiredMixin, ListView):
    model = Vacancy
    template_name = 'vacancy-list.html'

    def get_queryset(self):
        vacancies = super().get_queryset()
        vacancies = Vacancy.objects.filter(company__owner=self.request.user.id)
        return vacancies


class CompanyCreateView(LoginRequiredMixin, CreateView):
    model = Company
    template_name = 'company-edit.html'
    form_class = CompanyForm

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('vacancies:company-edit', args=(self.object.id,))


class CompanyEditView(LoginRequiredMixin, UpdateView):
    model = Company
    template_name = 'company-edit.html'
    form_class = CompanyForm

    def form_valid(self, form):
        messages.success(self.request, "some message")
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('vacancies:company-edit', args=(self.object.id,))


class CompanyView(DetailView):
    model = Company
    template_name = 'company.html'


class CompanyListView(ListView):
    model = Company
    template_name = 'companies.html'


class ResumeCreateView(LoginRequiredMixin, CreateView):
    model = Resume
    template_name = 'resume-edit.html'
    form_class = ResumeForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('vacancies:resume-edit', args=(self.object.id,))


class ResumeUpdateView(LoginRequiredMixin, UpdateView):
    model = Resume
    template_name = 'resume-edit.html'
    form_class = ResumeForm

    def form_valid(self, form):
        messages.success(self.request, "some message")
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('vacancies:resume-edit', args=(self.object.id,))


class VacancyListView(ListView):
    model = Vacancy
    template_name = 'vacancies.html'
    queryset = Vacancy.objects.order_by('-published_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Все вакансии"
        return context


class VacancyCatListView(ListView):
    model = Vacancy
    template_name = 'vacancies.html'

    def get_queryset(self):
        specialty = Specialty.objects.get(code=self.kwargs['category']).id
        return Vacancy.objects.filter(specialty=specialty).order_by('-published_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Specialty.objects.get(code=self.kwargs['category']).title
        return context


class VacancySearch(VacancyListView):
    template_name = 'search.html'

    def get_queryset(self):
        query = self.request.GET.get('search')
        return Vacancy.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        ).order_by('-published_at')
