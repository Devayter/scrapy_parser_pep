from pathlib import Path

RESULTS = 'results'

BASE_DIR = Path(__file__).parent
RESULTS_DIR = BASE_DIR / RESULTS

STATUS_SUMMARY = 'status_summary'
PEP = 'results/pep_%(time)s.csv'

BOT_NAME = 'pep_parse'

NEWSPIDER_MODULE = 'pep_parse.spiders'
SPIDER_MODULES = [NEWSPIDER_MODULE]

ROBOTSTXT_OBEY = True

FEEDS = {
    PEP: {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True,
    },
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
