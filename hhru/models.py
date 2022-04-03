from django.db import models
from django.db.models.fields import (
    BooleanField,
    CharField,
    DateTimeField,
    FloatField,
    IntegerField,
    TextField,
)
from django.db.models.fields.related import ManyToManyField

nb = dict(null=True, blank=True)


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


class Vacancy(models.Model):

    addresses_of_metro_stations = models.ManyToManyField(AddressMetroStation)
    driver_license_types = models.ManyToMantField(DriverLicenseType)
    professional_roles = models.ManyToMantField(ProfessionalRole)
    key_skills = models.ManyToMantField(KeySkill)
    specializations = models.ManyToMantField(Specialization)
    working_days = models.ManyToMantField(WorkingDay)
    working_time_interval = models.ManyToMantField(WorkingTimeInterval)
    working_time_modes = models.ManyToMantField(WorkingTimeMode)
    errors = models.ManyToMantField(Error)

    id = CharField(max_length=200, primary_key=True)
    premium = BooleanField()
    billing_type_id = CharField(max_length=200, **nb)
    billing_type_name = CharField(max_length=200, **nb)
    name = CharField(max_length=200, **nb)
    response_letter_required = BooleanField()
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
    allow_messages = BooleanField()
    site_id = CharField(max_length=200, **nb)
    site_name = CharField(max_length=200, **nb)
    experience_id = CharField(max_length=200, **nb)
    experience_name = CharField(max_length=200, **nb)
    schedule_id = CharField(max_length=200, **nb)
    schedule_name = CharField(max_length=200, **nb)
    employment_id = CharField(max_length=200, **nb)
    employment_name = CharField(max_length=200, **nb)
    description = TextField(**nb)
    accept_handicapped = BooleanField()
    accept_kids = BooleanField()
    archived = BooleanField()
    hidden = BooleanField()
    quick_responses_allowed = BooleanField()
    accept_incomplete_resumes = BooleanField()
    employer_id = CharField(max_length=200, **nb)
    employer_name = CharField(max_length=200, **nb)
    employer_url = CharField(max_length=200, **nb)
    employer_alternate_url = CharField(max_length=200, **nb)
    employer_logo_urls_240 = CharField(max_length=200, **nb)
    employer_logo_urls_90 = CharField(max_length=200, **nb)
    employer_logo_urls_original = CharField(max_length=200, **nb)
    employer_vacancies_url = CharField(max_length=200, **nb)
    employer_trusted = BooleanField()
    published_at = DateTimeField(**nb)
    created_at = DateTimeField(**nb)
    apply_alternate_url = CharField(max_length=200, **nb)
    has_test = BooleanField()
    alternate_url = CharField(max_length=200, **nb)
    accept_temporary = BooleanField()
    salary_from = IntegerField(**nb)
    salary_to = IntegerField(**nb)
    salary_currency = CharField(max_length=200, **nb)
    salary_gross = BooleanField()
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
