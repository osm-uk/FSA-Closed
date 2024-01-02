import csv
from typing import Iterable, List

import requests


def get_url(tag: str, page: int) -> str:
    return "https://taginfo.openstreetmap.org/api/4/key/values?key={}&filter=all&lang=en&sortname=count&sortorder=desc&rp=999&page={}".format(
        tag, page
    )


def get_values(tag: str) -> Iterable[List[int]]:
    data = requests.get(get_url(tag, 1)).json()
    while True:
        for value in data["data"]:
            for key in value["value"].split(";"):
                try:
                    yield [int(key)]
                except ValueError:
                    continue

        if data["rp"] != len(data["data"]):
            break
        data = requests.get(get_url(tag, data["page"] + 1)).json()


def main():
    with open("data/out_file.csv", "a") as file:
        writer = csv.writer(file)
        for tag in [
            "old_fhrs:id:2",
            "was:fhrs:id",
            "old:fhrs:id",
            "disused:fhrs:id",
            "old_fhrs:id",
        ]:
            writer.writerows(get_values(tag))


if __name__ == "__main__":
    main()
