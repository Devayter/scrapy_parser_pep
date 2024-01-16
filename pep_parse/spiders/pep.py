from urllib.parse import urlparse

import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    start_urls = ['https://peps.python.org/']
    allowed_domains = [urlparse(url).netloc
                       for url in start_urls]

    def parse(self, response):
        links = response.css(
            'section section#numerical-index tr td a::attr(href)'
        ).getall()
        for link in links:
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        h1_tag_splitted = response.css('h1.page-title::text').get().split('–')
        yield PepParseItem(
            number=h1_tag_splitted[0].replace('PEP', '').strip(),
            name=h1_tag_splitted[-1].strip(),
            status=response.css('#pep-content abbr::text').get()
        )
