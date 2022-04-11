import re
import json
import requests
import time

from hhru.models import Vacancy
import csv


def parse_hh(start_index: int, end_index: int, file_name: str):

    if not file_name.endswith(".csv"):
        print("Wrong file type")
        return

    csv_file = open(file_name, "r")
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

    for ind, line in enumerate(csv_file):
        row = list(csv.reader([line]))
        if ind < start_index:
            continue
        if ind > end_index:
            break
        try:
            api_url = row[11]
        except:
            api_url = (
                "https://api.hh.ru/vacancies/"
                + re.findall("\d+", line)[0]
                + "?host=hh.ru"
            )
        vacancy_raw = json.loads(session.get(api_url).content)
        time.sleep(0.1)

        Vacancy.create_with_all_fields(vacancy_raw)


#
