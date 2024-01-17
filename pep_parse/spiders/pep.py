import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://' + allowed_domains[0] + '/']

    def parse(self, response):
        links = response.css(
            'section section#numerical-index tr td a::attr(href)'
        ).getall()
        for link in links:
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        number, name = response.css('h1.page-title::text').get().split('–')
        yield PepParseItem(
            number=number.replace('PEP', '').strip(),
            name=name.strip(),
            status=response.css('#pep-content abbr::text').get()
        )
