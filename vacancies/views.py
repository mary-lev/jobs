from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {})

def list_vacancies(request):
    return render(request, 'vacancies.html', {})

def vacancy_category(request, category):
    return render(request, 'vacancies.html', {})

def company(request, company):
    return render(request, 'company.html', {})

def one_vacancy(request, vacancy):
    return render(request, 'vacancy.html', {})