import sys
sys.path.append("c:/Users/anew/stepik1/jobs/jobs/")
import os
import json
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'jobs.settings')
from transliterate import translit

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
            company['name'] = all['company']
            company['logo'] = all['company_logo']
            if 'location' in all.keys():
                company['location'] = all['location']
            else:
                company['location'] = 'Москва'
            company['employee_count'] = 100
            username = translit(all['company'].split(' ')[0], 'ru')
            if username not in User.objects.values_list('username', flat='true'):
                new_user = User.objects.create(username=username, password='admin')
                new_user.save()
            else:
                new_user = User.objects.get(username=username)
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
        if 'salary_min' in all.keys():
            new_vacancy['salary_min'] = all['salary_min']
        else:
            new_vacancy['salary_min'] = 1
        if 'salary_max' in all.keys():
            new_vacancy['salary_max'] = all['salary_max']
        else:
            new_vacancy['salary_max'] = 100
        new_vacancy['description'] = all['description']
        vacancy = Vacancy(**new_vacancy)
        vacancy.save()



if __name__== '__main__':
    main()

