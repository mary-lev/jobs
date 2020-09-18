from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    logo = models.ImageField(upload_to='company_images')
    description = models.CharField(max_length=100, blank=True, null=True)
    employee_count = models.IntegerField()
    owner = models.ForeignKey(User, related_name='companies', on_delete=models.CASCADE, null=True)


class Specialty(models.Model):
    code = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    picture = models.ImageField(upload_to='speciality_images', blank=True, null=True)


class Vacancy(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    specialty = models.ForeignKey(Specialty, related_name='vacancies', on_delete=models.CASCADE)
    company = models.ForeignKey(
        Company,
        related_name='vacancies',
        on_delete=models.CASCADE)
    skills = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateTimeField(auto_now=True)


class Application(models.Model):
    written_username = models.CharField(max_length=50)
    written_phone = models.CharField(max_length=10)
    written_cover_letter = models.TextField(max_length=1000)
    vacancy = models.ForeignKey(
        Vacancy,
        related_name='applications',
        on_delete=models.CASCADE)
    user = models.ForeignKey(
        User,
        related_name='applications',
        on_delete=models.CASCADE)


class Resume(models.Model):
    STATUS_CHOICES = (
        (1, 'Не ищу работу'),
        (2, 'Рассматриваю предложения'),
        (3, 'Ищу работу'),
        )
    GRADE_CHOICES = (
        (1, 'Стажер'),
        (2, 'Джуниор'),
        (3, 'Миддл'),
        (4, 'Синьор'),
        (5, 'Лид'),
        )
    user = models.ForeignKey(User, related_name='resumes', on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=30)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    salary = models.IntegerField()
    grade = models.CharField(max_length=1, choices=GRADE_CHOICES)
    education = models.TextField()
    experience = models.TextField()
    portfolio = models.TextField()
    
