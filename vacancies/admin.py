from django.contrib import admin

from .models import Vacancy, Specialty, Company, Application, Resume


class SpecialtyAdmin(admin.ModelAdmin):
    def __str__(self):
        return self.model.title


class ApplicationAdmin(admin.ModelAdmin):
    pass


class ResumeAdmin(admin.ModelAdmin):
    pass


class VacancyAdmin(admin.ModelAdmin):
    pass


class VacancyInline(admin.TabularInline):
    model = Vacancy


class CompanyAdmin(admin.ModelAdmin):
    inlines = (VacancyInline,)


admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(Specialty, SpecialtyAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(Resume, ResumeAdmin)
