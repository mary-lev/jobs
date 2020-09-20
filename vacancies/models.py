from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название компании')
    location = models.CharField(max_length=100, blank=True, verbose_name='География')
    logo = models.ImageField(upload_to='company_images', blank=True, verbose_name='Логотип')
    description = models.CharField(max_length=100, blank=True, verbose_name='Информация о компании')
    employee_count = models.IntegerField(verbose_name='Количество человек в компании', blank=True)
    owner = models.ForeignKey(User, related_name='companies', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Specialty(models.Model):
    code = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    picture = models.ImageField(upload_to='speciality_images', blank=True, null=True)

    def __str__(self):
        return self.title


class Vacancy(models.Model):
    title = models.CharField(max_length=40, blank=True, null=True, verbose_name='Название вакансии')
    specialty = models.ForeignKey(
        Specialty,
        related_name='vacancies',
        on_delete=models.CASCADE,
        verbose_name='Специализация')
    company = models.ForeignKey(
        Company,
        related_name='vacancies',
        on_delete=models.CASCADE,
        verbose_name='Название компании')
    skills = models.CharField(
        max_length=1000,
        blank=True,
        null=True,
        verbose_name='Требуемые навыки')
    description = models.CharField(
        max_length=10000,
        blank=True, null=True,
        verbose_name='Описание вакансии')
    salary_min = models.IntegerField(verbose_name='Зарплата от')
    salary_max = models.IntegerField(verbose_name='Зарплата до')
    published_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Application(models.Model):
    written_username = models.CharField(max_length=50, verbose_name='Вас зовут')
    written_phone = models.CharField(max_length=10, verbose_name='Ваш телефон')
    written_cover_letter = models.TextField(
        max_length=1000,
        verbose_name='Сопроводительное письмо')
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
        ('1', 'Не ищу работу'),
        ('2', 'Рассматриваю предложения'),
        ('3', 'Ищу работу'),
        )
    GRADE_CHOICES = (
        ('1', 'Стажер'),
        ('2', 'Джуниор'),
        ('3', 'Миддл'),
        ('4', 'Синьор'),
        ('5', 'Лид'),
        )
    user = models.ForeignKey(User, related_name='resumes', on_delete=models.CASCADE)
    name = models.CharField(max_length=20, verbose_name='Имя')
    surname = models.CharField(max_length=30, verbose_name='Фамилия')
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        verbose_name='Готовность к работе')
    salary = models.IntegerField(verbose_name='Ожидаемое вознаграждение')
    specialty = models.ForeignKey(Specialty, related_name='resumes', on_delete=models.CASCADE)
    grade = models.CharField(max_length=1, choices=GRADE_CHOICES, verbose_name='Квалификация')
    education = models.TextField(verbose_name='Образование')
    experience = models.TextField(verbose_name='Опыт работы')
    portfolio = models.CharField(max_length=100, verbose_name='Ссылка на портфолио')
