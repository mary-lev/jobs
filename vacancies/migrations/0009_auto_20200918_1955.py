# Generated by Django 3.1.1 on 2020-09-18 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0008_auto_20200918_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancies', to='vacancies.company', verbose_name='Название компании'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Описание вакансии'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='salary_max',
            field=models.IntegerField(verbose_name='Зарплата до'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='salary_min',
            field=models.IntegerField(verbose_name='Зарплата от'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='skills',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Требуемые навыки'),
        ),
    ]
