import base64
import json
import logging
import urllib.request

from env import ALIBABA_URL
from feeders.base import Source
from helper.readable import translate
from helper.utils import dict2html, send_email


class AlibabaSource(Source):
    def __init__(self, filters: dict):
        self.filters = filters

    def load_data(self):
        try:
            url = urllib.request.urlopen(
                ALIBABA_URL + base64.urlsafe_b64encode(json.dumps(self.filters).encode()).decode())
            return json.loads(url.read().decode())
        except urllib.error.HTTPError:
            raise ValueError(' سرویس راه‌آهن قطع می باشد.')

    def parse(self):
        data = self.load_data()
        columns = get_columns()
        result = data.get('result')
        if result:
            departing = result.get('departing')
            return [{translate(k): v for k, v in item.items() if k in columns} for item in departing if
                    item['seat'] > 0]
        return False

    def notify(self):
        data = self.parse()
        print(data)
        if data:
            message = dict2html(data) if data else \
                "<h1 style='background-color: red; color: white'> Server is down! </h1> "
            send_email(message)


def get_columns():
    return ['originName',
            'destinationName',
            'trainNumber',
            'departureDateTime',
            'arrivalDateTime',
            'cost',
            'fullPrice',
            'seat',
            ]
