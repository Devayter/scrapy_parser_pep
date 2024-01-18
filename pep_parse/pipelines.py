import csv
from collections import defaultdict
from datetime import datetime as dt

from .settings import BASE_DIR, RESULTS, RESULTS_DIR, STATUS_SUMMARY


RESULTS_DIR.mkdir(exist_ok=True)


class PepParsePipeline:

    def open_spider(self, spider):
        self.statuses = defaultdict(int)

    def process_item(self, item, spider):
        self.statuses[item.get('status')] += 1
        return item

    def close_spider(self, spider):
        current_time = dt.now().strftime('%Y-%m-%d_%H-%M-%S')
        file_name = f'{STATUS_SUMMARY}_{current_time}.csv'
        file_path = BASE_DIR / RESULTS / file_name
        with open(file_path, mode='w', encoding='utf-8') as csvfile:
            csv.writer(
                csvfile,
                dialect=csv.unix_dialect,
                quoting=csv.QUOTE_NONE
            ).writerows([
                ('Статус', 'Количество'),
                *self.statuses.items(),
                ('Всего', sum(self.statuses.values()))
            ])
