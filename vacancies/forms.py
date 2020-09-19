from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Column
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Application, Company, Vacancy, Specialty, Resume


class LoginForm(AuthenticationForm):

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].label = 'Логин'

        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Войти', css_class='btn btn-primary btn-lg btn-block'))

        self.helper.form_class = 'form-signin pt-5'
        self.helper.label_class = 'text-muted'


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2', ]:
            self.fields[fieldname].help_text = None

        self.fields['username'].label = 'Логин'

        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Зарегистрироваться', css_class="btn btn-primary btn-lg btn-block"))

        self.helper.form_class = 'form-signin pt-5'
        self.helper.label_class = 'text-muted'


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['written_username', 'written_phone', 'written_cover_letter']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Отправить отклик', css_class='btn btn-primary mt-4 mb-2'))

        self.helper.form_class = 'card mt-4 mb-3'
        self.helper.label_class = 'mb-1'


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'employee_count', 'location', 'description', 'logo']
        widgets = {
        'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Сохранить', css_class='btn btn-info'))

        self.helper.form_class = 'col-12 col-md-6'
        self.helper.label_class = 'mb-2 text-dark'


class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ['title', 'specialty', 'salary_min', 'salary_max', 'skills', 'description']
        widgets = {
        'specialty': forms.Select(attrs={'class': 'custom-select mr-sm-2'}),
        'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        specialties = Specialty.objects.all()
        specialty_names = [(specialty.id, specialty.title) for specialty in specialties]
        self.fields['specialty'].choices=specialty_names

        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.label_class = 'mb-2 text-dark'
        self.helper.field_class = '"form-control"'

        self.helper.layout = Layout(
            Row(
                Column('title', css_class='col-12 col-md-6'),
                Column('specialty', css_class='col-12 col-md-6'),
                css_class='row'
                ),
            Row(
                Column('salary_min', css_class='col-12 col-md-6'),
                Column('salary_max', css_class='col-12 col-md-6'),
                css_class='row'
                ),
            'skills',
            'description',
            Submit('submit', 'Сохранить', css_class='btn btn-info')
                )


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['name', 'surname', 'status', 'salary', 'grade', 'specialty', 'education', 'experience', 'portfolio']
        widgets = {
            'status': forms.Select(attrs={'class': 'select'}),
            'grade': forms.Select(attrs={'class': 'select'}),
            'education': forms.Textarea(attrs={'class': 'form-control text-uppercase'}),
            'experience': forms.Textarea(attrs={'rows': "4"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = "POST"
        self.helper.label_class = 'mb-2 text-dark'
        self.helper.form_show_errors = True

        self.helper.layout = Layout(
            Row(
                Column('name', css_class='col-12 col-md-6'),
                Column('surname', css_class='col-12 col-md-6'),
                css_class='row'
                ),
            Row(
                Column('status', css_class='col-12 col-md-6'),
                Column('salary', css_class='col-12 col-md-6'),
                css_class='row'
                ),
            Row(
                Column('specialty', css_class='col-12 col-md-6'),
                Column('grade', css_class='col-12 col-md-6'),
                css_class='row'
                ),
            'education',
            'experience',
            'portfolio',
            Submit('submit', 'Сохранить', css_class='btn btn-info')
            )
