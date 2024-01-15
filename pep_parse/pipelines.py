import csv
from collections import defaultdict
from datetime import datetime as dt

from constants import BASE_DIR, RESULTS, STATUS_SUMMARY


class PepParsePipeline:

    def __init__(self):
        self.statuses = defaultdict(int)

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        status = item.get('status')
        if status:
            self.statuses[status] += 1
        return item

    def close_spider(self, spider):
        current_time = dt.now().strftime('%Y-%m-%d_%H-%M-%S')
        file_name = f'{STATUS_SUMMARY}_{current_time}.csv'
        file_path = BASE_DIR / RESULTS / file_name
        with open(file_path, mode='w', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile, delimiter='"', quoting=csv.QUOTE_NONE)
            writer.writerow(['Статус: Количество'])
            for status, count in self.statuses.items():
                writer.writerow([f'{status}: {count}'])
            writer.writerow([f'Всего: {sum(self.statuses.values())}'])
