from django.contrib import admin
from django.urls import path
from .views import process_csv_form

from hhru.models import (
    Vacancy,
    AddressMetroStation,
    DriverLicenseType,
    ProfessionalRole,
    KeySkill,
    Specialization,
    WorkingDay,
    WorkingTimeInterval,
    WorkingTimeMode,
    Error,
)

# Register your models here.


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    def get_urls(self):
        urls = super().get_urls()
        new_urls = [
            path("upload-csv/", process_csv_form),
        ]
        return new_urls + urls


@admin.register(AddressMetroStation)
class AddressMetroStationAdmin(admin.ModelAdmin):
    pass


@admin.register(DriverLicenseType)
class DriverLicenseTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(ProfessionalRole)
class ProfessionalRoleAdmin(admin.ModelAdmin):
    pass


@admin.register(KeySkill)
class KeySkillAdmin(admin.ModelAdmin):
    pass


@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    pass


@admin.register(WorkingDay)
class WorkingDayAdmin(admin.ModelAdmin):
    pass


@admin.register(WorkingTimeInterval)
class WorkingTimeIntervalAdmin(admin.ModelAdmin):
    pass


@admin.register(WorkingTimeMode)
class WorkingTimeModeAdmin(admin.ModelAdmin):
    pass


@admin.register(Error)
class ErrorAdmin(admin.ModelAdmin):
    pass
