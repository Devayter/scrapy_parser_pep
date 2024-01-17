import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import RESULTS_DIR


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = [f'https://{domain}/' for domain in allowed_domains]

    def start_requests(self):
        RESULTS_DIR.mkdir(exist_ok=True)
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        for link in response.css(
            'section section#numerical-index tr td a::attr(href)'
        ).getall():
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        number, name = response.css('h1.page-title::text').get().split('–')
        yield PepParseItem(
            number=number.replace('PEP', '').strip(),
            name=name.strip(),
            status=response.css('#pep-content abbr::text').get()
        )
