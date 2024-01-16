import csv
import os
from collections import defaultdict
from datetime import datetime as dt

from settings import BASE_DIR, RESULTS, STATUS_SUMMARY


class PepParsePipeline:

    def open_spider(self, spider):
        self.folder_path = BASE_DIR / RESULTS
        if not os.path.isdir(self.folder_path):
            self.folder_path.mkdir()
        self.statuses = defaultdict(int)

    def process_item(self, item, spider):
        self.statuses[item.get('status')] += 1
        return item

    def close_spider(self, spider):
        current_time = dt.now().strftime('%Y-%m-%d_%H-%M-%S')
        file_name = f'{STATUS_SUMMARY}_{current_time}.csv'
        file_path = self.folder_path / file_name
        with open(file_path, mode='w', encoding='utf-8') as csvfile:
            csv.writer(
                csvfile,
                dialect=csv.unix_dialect,
                quoting=csv.QUOTE_NONE
            ).writerows([('Статус', 'Количество'),
                        *self.statuses.items(),
                        ('Всего', sum(self.statuses.values()))])
