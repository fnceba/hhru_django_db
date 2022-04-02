from django.db import models
from django.db.models.fields import BooleanField, CharField, DateTimeField, FloatField, IntegerField

# it ain't much, but it's honest work

#! - надо подробнее чекнуть, что это
### - нужно создать отдельную модель
class Vacancy(models.Model):
    id = IntegerField(primary_key=True)
    name = CharField(max_length=1000)
    has_test = BooleanField()
    response_letter_required = BooleanField()
    salary_from = IntegerField(blank=True)
    salary_to = IntegerField(blank=True)
    salary_currency = CharField(blank=True)
    salary_gross = BooleanField(blank=True)
    published_at = DateTimeField()
    created_at = DateTimeField()
    parsed_at = DateTimeField()
    url = CharField(max_length=100)
    employer_name = CharField(max_length=1000)
    description = CharField()
    alternate_url = CharField(max_length=100)
    area_id = IntegerField()
    area_name = CharField(max_length=100)

    accept_handicapped = BooleanField()
    accept_incomplete_resumes = BooleanField()
    accept_kids = BooleanField()
    accept_temporary = BooleanField()

    address_building = CharField(max_length=100, blank=True)
    address_city = CharField(max_length=100, blank=True)
    address_lat = FloatField(blank=True)
    address_lng = FloatField(blank=True)
    address_metro_station_name = CharField(max_length=100, blank=True)
    address_metro_lat = FloatField(blank=True)
    address_metro_lng = FloatField(blank=True)
    address_metro_line_name = CharField(max_length=100, blank=True)
    address_metro_line_id = CharField(max_length=100, blank=True)
    address_metro_station_id  = CharField(max_length=100, blank=True)
    address_metro_station_name = CharField(max_length=100, blank=True)
    address_raw = CharField(max_length=1000, blank=True)
    address_street = CharField(max_length=100, blank=True)
    #!address_description
    
    ###address_metro_stations
    
    allow_messages = BooleanField()
    api_alternate_url = CharField(max_length=100)
    api_apply_alternate_url = CharField(max_length=100, blank=True)
    archived = BooleanField()
    api_area_id = CharField(max_length=100)
    api_area_name = CharField(max_length=100)
    api_area_url = CharField(max_length=100)

    billing_type_id = CharField(max_length=100)
    billing_type_name = CharField(max_length=100)

    #!branded_description
    #!code
    #!contacts
    api_created_at = DateTimeField()
    #!department
    api_description = CharField() 

    ###driver_license_types
'''
    employer_
    employer_
    employer_
    employer_
    employer_
    employer_
    employer_
'''