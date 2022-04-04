from typing import Any
import csv

nb = dict(null=True, blank=True)


def dicts_into_primitive_fields(vacancy_raw: dict, prefix="") -> Any:
    for key, value in vacancy_raw.items():
        if type(value) is dict:
            yield from dicts_into_primitive_fields(value, prefix=prefix + key + "_")
        elif value != None:
            yield (prefix + key, value)


def csv_iter(line_iter):
    line = next(line_iter, b"stop").decode()
    while line != "stop":
        yield from list(csv.reader([line]))
        line = next(line_iter, b"stop").decode()
