import json
from os import path
from datetime import date, timedelta
from tqdm import tqdm
from data_for_day import get_for_day
import requests


def get_dates(start_date, end_date=date.today()):
    delta = timedelta(days=1)

    while start_date <= end_date:
        yield end_date
        end_date -= delta


def main(session):
    r = tqdm(get_dates(date(2007, 1, 16)))

    for curr_date in r:
        r.set_description(curr_date.strftime("%Y-%m-%d"))
        path_to_file = f'data/{curr_date.strftime("%Y-%m-%d")}.json'
        if not path.isfile(path_to_file):
            with open(path_to_file, 'w', encoding='utf-8') as f:
                json.dump(get_for_day(curr_date, session), f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    main(requests.Session())

