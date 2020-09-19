import sys
sys.path.append("c:/Users/anew/stepik1/jobs/jobs/")
import os
import json
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'jobs.settings')

import django
django.setup()

from django.contrib.auth.models import User
from vacancies.models import Company, Vacancy, Specialty
    #vacancy['title']
    #vacancy['location']
    #vacancy['company']
    #vacancy['company_logo']
    #vacancy['specialty']
    #vacancy['skills']
    #vacancy['salary_min']
    #vacancy['salary_max']

def main():
    with open('vacancies.json', 'r', encoding='utf-8') as f:
        vacancies = json.load(f)

    specialties = Specialty.objects.values_list('title', flat='true')
    print(specialties)
    for all in vacancies:
        new_vacancy = {}
        if all['company'] not in Company.objects.values_list('name', flat='true'):
            print(all['company'])
            company = {}
            company['title'] = all['company']
            company['logo'] = all['company_logo']
            company['location'] = all['location']
            new_user = Users.objects.create(username=all['company'], password='admin')
            new_user.save()
            company['owner'] = new_user
            new_company = Company(**company)
            new_company.save()
            new_vacancy['company'] = new_company
        else:
            new_vacancy['company'] = Company.objects.get(name=all['company'])
        new_vacancy['title'] = all['title']
        if all['specialty'] not in specialties:
            new_vacancy['specialty'] = Specialty.objects.get(title='Девопс')
        else:
            new_vacancy['specialty'] = Specialty.objects.get(title=all['specialty'])
        new_vacancy['skills'] = all['skills']
        new_vacancy['salary_min'] = all['salary_min']
        new_vacancy['salary_max'] = all['salary_max']
        new_vacancy['description'] = all['description']
        vacancy = Vacancy(**new_vacancy)
        vacancy.save()



if __name__== '__main__':
    main()

