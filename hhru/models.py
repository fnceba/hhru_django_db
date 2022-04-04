from django.db import models
from django.db.models.fields import (
    BooleanField,
    CharField,
    DateTimeField,
    FloatField,
    IntegerField,
    TextField,
)

from hhru.utils import dicts_into_primitive_fields, nb


class AddressMetroStation(models.Model):
    station_name = CharField(max_length=200, **nb)
    line_name = CharField(max_length=200, **nb)
    station_id = CharField(max_length=200, **nb)
    line_id = CharField(max_length=200, **nb)
    lat = FloatField(**nb)
    lng = FloatField(**nb)


class DriverLicenseType(models.Model):
    id = CharField(max_length=200, primary_key=True)


class ProfessionalRole(models.Model):
    id = CharField(max_length=200, primary_key=True)
    name = CharField(max_length=200, **nb)


class KeySkill(models.Model):
    name = CharField(max_length=200, **nb)


class Specialization(models.Model):
    id = CharField(max_length=200, primary_key=True)
    name = CharField(max_length=200, **nb)
    profarea_id = CharField(max_length=200, **nb)
    profarea_name = CharField(max_length=200, **nb)


class WorkingDay(models.Model):
    id = CharField(max_length=200, primary_key=True)
    name = CharField(max_length=200, **nb)


class WorkingTimeInterval(models.Model):
    id = CharField(max_length=200, primary_key=True)
    name = CharField(max_length=200, **nb)


class WorkingTimeMode(models.Model):
    id = CharField(max_length=200, primary_key=True)
    name = CharField(max_length=200, **nb)


class Error(models.Model):
    type = CharField(max_length=200, **nb)


json_name_to_class = {
    "address_metro_stations": AddressMetroStation,
    "driver_license_types": DriverLicenseType,
    "professional_roles": ProfessionalRole,
    "key_skills": KeySkill,
    "specializations": Specialization,
    "working_days": WorkingDay,
    "working_time_intervals": WorkingTimeInterval,
    "working_time_modes": WorkingTimeMode,
    "errors": Error,
}


class Vacancy(models.Model):

    address_metro_stations = models.ManyToManyField(AddressMetroStation, **nb)
    driver_license_types = models.ManyToManyField(DriverLicenseType, **nb)
    professional_roles = models.ManyToManyField(ProfessionalRole, **nb)
    key_skills = models.ManyToManyField(KeySkill, **nb)
    specializations = models.ManyToManyField(Specialization, **nb)
    working_days = models.ManyToManyField(WorkingDay, **nb)
    working_time_intervals = models.ManyToManyField(WorkingTimeInterval, **nb)
    working_time_modes = models.ManyToManyField(WorkingTimeMode, **nb)
    errors = models.ManyToManyField(Error, **nb)

    id = CharField(max_length=200, primary_key=True)
    premium = BooleanField(**nb)
    billing_type_id = CharField(max_length=200, **nb)
    billing_type_name = CharField(max_length=200, **nb)
    name = CharField(max_length=200, **nb)
    response_letter_required = BooleanField(**nb)
    area_id = CharField(max_length=200, **nb)
    area_name = CharField(max_length=200, **nb)
    area_url = CharField(max_length=200, **nb)
    type_id = CharField(max_length=200, **nb)
    type_name = CharField(max_length=200, **nb)
    address_city = CharField(max_length=200, **nb)
    address_street = CharField(max_length=200, **nb)
    address_building = CharField(max_length=200, **nb)
    address_lat = FloatField(**nb)
    address_lng = FloatField(**nb)
    address_raw = CharField(max_length=200, **nb)
    allow_messages = BooleanField(**nb)
    site_id = CharField(max_length=200, **nb)
    site_name = CharField(max_length=200, **nb)
    experience_id = CharField(max_length=200, **nb)
    experience_name = CharField(max_length=200, **nb)
    schedule_id = CharField(max_length=200, **nb)
    schedule_name = CharField(max_length=200, **nb)
    employment_id = CharField(max_length=200, **nb)
    employment_name = CharField(max_length=200, **nb)
    description = TextField(**nb)
    accept_handicapped = BooleanField(**nb)
    accept_kids = BooleanField(**nb)
    archived = BooleanField(**nb)
    hidden = BooleanField(**nb)
    quick_responses_allowed = BooleanField(**nb)
    accept_incomplete_resumes = BooleanField(**nb)
    employer_id = CharField(max_length=200, **nb)
    employer_name = CharField(max_length=200, **nb)
    employer_url = CharField(max_length=200, **nb)
    employer_alternate_url = CharField(max_length=200, **nb)
    employer_logo_urls_240 = CharField(max_length=200, **nb)
    employer_logo_urls_90 = CharField(max_length=200, **nb)
    employer_logo_urls_original = CharField(max_length=200, **nb)
    employer_vacancies_url = CharField(max_length=200, **nb)
    employer_trusted = BooleanField(**nb)
    published_at = DateTimeField(**nb)
    created_at = DateTimeField(**nb)
    apply_alternate_url = CharField(max_length=200, **nb)
    has_test = BooleanField(**nb)
    alternate_url = CharField(max_length=200, **nb)
    accept_temporary = BooleanField(**nb)
    salary_from = IntegerField(**nb)
    salary_to = IntegerField(**nb)
    salary_currency = CharField(max_length=200, **nb)
    salary_gross = BooleanField(**nb)
    department_id = CharField(max_length=200, **nb)
    department_name = CharField(max_length=200, **nb)
    address_metro_station_name = CharField(max_length=200, **nb)
    address_metro_line_name = CharField(max_length=200, **nb)
    address_metro_station_id = CharField(max_length=200, **nb)
    address_metro_line_id = CharField(max_length=200, **nb)
    address_metro_lat = FloatField(**nb)
    address_metro_lng = FloatField(**nb)
    branded_description = TextField(**nb)
    request_id = CharField(max_length=200, **nb)
    code = CharField(max_length=200, **nb)
    insider_interview_id = CharField(max_length=200, **nb)
    insider_interview_url = CharField(max_length=200, **nb)
    vacancy_constructor_template_id = IntegerField(**nb)
    vacancy_constructor_template_name = CharField(max_length=200, **nb)
    vacancy_constructor_template_top_picture_height = IntegerField(**nb)
    vacancy_constructor_template_top_picture_width = IntegerField(**nb)
    vacancy_constructor_template_top_picture_path = CharField(max_length=200, **nb)
    vacancy_constructor_template_top_picture_blurred_path = CharField(
        max_length=200, **nb
    )

    class Meta:
        verbose_name_plural = "Vacancies"

    @classmethod
    def create_with_all_fields(cls, vacancy_raw: dict) -> None:
        fields = list(dicts_into_primitive_fields(vacancy_raw))
        fil = dict(filter(lambda item: type(item[1]) != list, fields))
        if "id" not in fil:
            return
        vacancy, _ = cls.objects.get_or_create(**fil)
        vacancy.save()
        for item in filter(
            lambda item: type(item[1]) == list and len(item[1]) > 0, fields
        ):
            for field in map(
                lambda d: json_name_to_class[item[0]].objects.get_or_create(**d)[0],
                item[1],
            ):
                vacancy.__getattribute__(item[0]).add(field)
