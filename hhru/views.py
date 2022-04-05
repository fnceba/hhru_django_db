from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
import json
import requests
import re
import time

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

            session = requests.session()
            session.headers = {
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "cache-control": "max-age=0",
                "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"Linux"',
                "sec-fetch-dest": "document",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "cross-site",
                "sec-fetch-user": "?1",
                "upgrade-insecure-requests": "1",
                "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
            }

            for ind, row in enumerate(csv_iter(csv_file.__iter__())):
                if ind < start_index:
                    continue
                if ind > end_index:
                    break
                try:
                    api_url = row[11]
                except:
                    api_url = re.findall("\d+", " ".join(row))[0]
                vacancy_raw = json.loads(session.get(api_url).content)
                time.sleep(0.1)

                Vacancy.create_with_all_fields(vacancy_raw)
            return HttpResponseRedirect("/admin/hhru/vacancy")

    else:
        form = ReadFromCSVForm()

    return render(request, "admin/upload_csv_form.html", {"form": form})
