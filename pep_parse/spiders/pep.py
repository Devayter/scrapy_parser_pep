import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        tr_tags = response.css('section section#numerical-index tr')
        for pep in tr_tags[1:]:
            link = pep.css('td a::attr(href)').get()
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        yield PepParseItem({
            'number': (
                response.css('h1.page-title::text')
                .get().split('–')[0].replace('PEP', '').strip()
            ),
            'name': (
                response.css('h1.page-title::text')
                .get().split('–')[-1].strip()
            ),
            'status': response.css('#pep-content abbr::text').get()
        })
