from django.db import models
from django.db.models.fields import (
    BooleanField,
    CharField,
    DateTimeField,
    FloatField,
    IntegerField,
    TextField,
)

# it ain't much, but it's honest work
nb = dict(null=True, blank=True)
#! - надо подробнее чекнуть, что это
### - нужно создать отдельную модель
class Vacancy(models.Model):
    id = CharField(max_length=100, **nb)
    premium = BooleanField()
    billing_type_id = CharField(max_length=100, **nb)
    billing_type_name = CharField(max_length=100, **nb)
    name = CharField(max_length=100, **nb)
    response_letter_required = BooleanField()
    area_id = CharField(max_length=100, **nb)
    area_name = CharField(max_length=100, **nb)
    area_url = CharField(max_length=100, **nb)
    type_id = CharField(max_length=100, **nb)
    type_name = CharField(max_length=100, **nb)
    address_city = CharField(max_length=100, **nb)
    address_street = CharField(max_length=100, **nb)
    address_building = CharField(max_length=100, **nb)
    address_lat = FloatField(**nb)
    address_lng = FloatField(**nb)
    address_raw = CharField(max_length=100, **nb)
    allow_messages = BooleanField()
    site_id = CharField(max_length=100, **nb)
    site_name = CharField(max_length=100, **nb)
    experience_id = CharField(max_length=100, **nb)
    experience_name = CharField(max_length=100, **nb)
    schedule_id = CharField(max_length=100, **nb)
    schedule_name = CharField(max_length=100, **nb)
    employment_id = CharField(max_length=100, **nb)
    employment_name = CharField(max_length=100, **nb)
    description = TextField(**nb)
    accept_handicapped = BooleanField()
    accept_kids = BooleanField()
    archived = BooleanField()
    hidden = BooleanField()
    quick_responses_allowed = BooleanField()
    accept_incomplete_resumes = BooleanField()
    employer_id = CharField(max_length=100, **nb)
    employer_name = CharField(max_length=100, **nb)
    employer_url = CharField(max_length=100, **nb)
    employer_alternate_url = CharField(max_length=100, **nb)
    employer_logo_urls_240 = CharField(max_length=100, **nb)
    employer_logo_urls_90 = CharField(max_length=100, **nb)
    employer_logo_urls_original = CharField(max_length=100, **nb)
    employer_vacancies_url = CharField(max_length=100, **nb)
    employer_trusted = BooleanField()
    published_at = DateTimeField(**nb)
    created_at = DateTimeField(**nb)
    apply_alternate_url = CharField(max_length=100, **nb)
    has_test = BooleanField()
    alternate_url = CharField(max_length=100, **nb)
    accept_temporary = BooleanField()
    salary_from = IntegerField(**nb)
    salary_to = IntegerField(**nb)
    salary_currency = CharField(max_length=100, **nb)
    salary_gross = BooleanField()
    department_id = CharField(max_length=100, **nb)
    department_name = CharField(max_length=100, **nb)
    address_metro_station_name = CharField(max_length=100, **nb)
    address_metro_line_name = CharField(max_length=100, **nb)
    address_metro_station_id = CharField(max_length=100, **nb)
    address_metro_line_id = CharField(max_length=100, **nb)
    address_metro_lat = FloatField(**nb)
    address_metro_lng = FloatField(**nb)
    branded_description = TextField(**nb)
    request_id = CharField(max_length=100, **nb)
    code = CharField(max_length=100, **nb)


class AddressMetroStations(models.Model):
    station_name = CharField(max_length=100, **nb)
    line_name = CharField(max_length=100, **nb)
    station_id = CharField(max_length=100, **nb)
    line_id = CharField(max_length=100, **nb)
    lat = FloatField(**nb)
    lng = FloatField(**nb)


class KeySkills(models.Model):
    name = CharField(max_length=100, **nb)


class Specializations(models.Model):
    id = CharField(max_length=100, **nb)
    name = CharField(max_length=100, **nb)
    profarea_id = CharField(max_length=100, **nb)
    profarea_name = CharField(max_length=100, **nb)


class ProfessionalRoles(models.Model):
    id = CharField(max_length=100, **nb)
    name = CharField(max_length=100, **nb)


class Errors(models.Model):
    type = CharField(max_length=100, **nb)
