from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Field, Div
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import Application, Company, Vacancy

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

        for fieldname in ['username', 'password1', 'password2',]:
            self.fields[fieldname].help_text = None

        self.fields['username'].label = 'Логин'

        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Зарегистрироваться', css_class="btn btn-primary btn-lg btn-block"))

        self.helper.form_class = 'form-signin pt-5'
        self.helper.label_class = 'text-muted'


class VacancySend(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['written_username','written_phone', 'written_cover_letter']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        self.fields['written_username'].label = 'Вас зовут'
        self.fields['written_phone'].label = 'Ваш телефон'
        self.fields['written_cover_letter'].label = 'Сопроводительное письмо'

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
        'name': forms.TextInput(attrs={'class': 'form-control'}),
        'employee_count': forms.TextInput(attrs={'class': 'form-control'}),
        'location': forms.TextInput(attrs={'class': 'form-control'}),
        'description': forms.Textarea(attrs={'class': 'form-control'}),
        #'logo': forms.ClearableFileInput(attrs={'class': 'btn btn-info px-4', 'style': 'visibility:hidden;'}),
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].label = 'Название компании'
        self.fields['employee_count'].label = 'Количество человек в компании'
        self.fields['location'].label = 'География'
        self.fields['description'].label = 'Информация о компании'
        self.fields['logo'].label = 'Логотип'

        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Сохранить', css_class='btn btn-info'))

        self.helper.form_class = 'col-12 col-md-6'
        self.helper.label_class = 'mb-2 text-dark'
        self.helper.field_class = 'form-control'


class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ['title', 'specialty']