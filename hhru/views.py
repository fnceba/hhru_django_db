from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
import json
import requests

from hhru.utils import csv_iter

from .forms import ReadFromCSVForm
from .models import Vacancy

# Create your views here.


def process_csv_form(request):
    if request.method == "POST":
        form = ReadFromCSVForm(request.POST, request.FILES)
        if form.is_valid():
            start_index = int(form.data["start_index"]) + 1
            end_index = int(form.data["end_index"]) + 1
            csv_file = request.FILES["csv_file"]

            if not csv_file.name.endswith(".csv"):
                messages.warning(request, "The wrong file type was uploaded")
                return HttpResponseRedirect(request.path_info)

            for ind, row in enumerate(csv_iter(csv_file.__iter__())):
                if ind < start_index:
                    continue
                if ind > end_index:
                    break
                vacancy_raw = json.loads(requests.get(row[11]).content)
                Vacancy.create_with_all_fields(vacancy_raw)
            return HttpResponseRedirect("/admin/hhru/vacancy")

    else:
        form = ReadFromCSVForm()

    return render(request, "admin/upload_csv_form.html", {"form": form})
