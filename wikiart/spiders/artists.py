# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector

from wikiart.items import WikiartItem


class ArtistsSpider(scrapy.Spider):
    name = "artists"
    allowed_domains = ["wikiart.org"]
    start_urls = (
        'http://www.wikiart.org/en/Alphabet/A',
        'http://www.wikiart.org/en/Alphabet/B',
        'http://www.wikiart.org/en/Alphabet/C',
        'http://www.wikiart.org/en/Alphabet/D',
        'http://www.wikiart.org/en/Alphabet/E',
        'http://www.wikiart.org/en/Alphabet/F',
        'http://www.wikiart.org/en/Alphabet/G',
        'http://www.wikiart.org/en/Alphabet/H',
        'http://www.wikiart.org/en/Alphabet/I',
        'http://www.wikiart.org/en/Alphabet/J',
        'http://www.wikiart.org/en/Alphabet/K',
        'http://www.wikiart.org/en/Alphabet/L',
        'http://www.wikiart.org/en/Alphabet/M',
        'http://www.wikiart.org/en/Alphabet/N',
        'http://www.wikiart.org/en/Alphabet/O',
        'http://www.wikiart.org/en/Alphabet/P',
        'http://www.wikiart.org/en/Alphabet/Q',
        'http://www.wikiart.org/en/Alphabet/R',
        'http://www.wikiart.org/en/Alphabet/S',
        'http://www.wikiart.org/en/Alphabet/T',
        'http://www.wikiart.org/en/Alphabet/U',
        'http://www.wikiart.org/en/Alphabet/V',
        'http://www.wikiart.org/en/Alphabet/W',
        'http://www.wikiart.org/en/Alphabet/X',
        'http://www.wikiart.org/en/Alphabet/Y',
        'http://www.wikiart.org/en/Alphabet/Z',
        'http://www.wikiart.org/en/Alphabet/3',
    )

    def parse(self, response):
        #conn, cur = DBUtils.get_conn()
        hxs = HtmlXPathSelector(response)

        for sel in hxs.select("//div[@class='pozRel']"):

            link = "http://www.wikiart.org"
            linkArray = sel.xpath('a/@href').extract()

            link += linkArray[0]

            yield Request(url=link, callback=self.parse_artist)

            #sql = "INSERT INTO artists(artist_url) VALUES (\'"+ link + "\')"
            #cur.execute(sql)
            #conn.commit()
            #print link, imgsrc.encode('utf-8')

        #cur.close()
        #conn.close()

    def parse_artist(self, response):
        artist = WikiartItem()

        artist['artist_url'] = response._url

        hxs = HtmlXPathSelector(response)
        artist['artist_name'] = hxs.select("//div[@class='tt30']").xpath("h1/text()").extract()[0]
        artist['artist_avatar'] = hxs.xpath("//div[@class='pozRel']/img/@src").extract()[0]

        profile = hxs.select("//div[@class='DataProfileBox']")
        #born1 = profile.xpath("p[1]/text()").extract()
        born = profile.xpath("//span[@itemprop='birthDate']/text()").extract()
        if len(born) > 0:
            artist['born'] = born[0]
        else:
            artist['born'] = 'UnKnown'

        died = profile.xpath("//span[@itemprop='dearthDate']/text()").extract()
        if len(died) > 0:
            artist['died'] = died[0]
        else:
            artist['died'] = 'UnKnown'

        nationality = profile.xpath("//span[@itemprop='nation']/text()").extract()
        if len(nationality) > 0:
            artist['nationality'] = nationality[0]
        else:
            artist['nationality'] = 'UnKnown'

        return artist





