# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector

from wikiart.items import WikiartItem
from wikiart.items import WikiartProductsItem


class ArtistsSpider(scrapy.Spider):
    _link = "http://www.wikiart.org"
    name = "artists"
    allowed_domains = ["wikiart.org"]
    start_urls = (
        'http://www.wikiart.org/en/Alphabet/A',
        #'http://www.wikiart.org/en/Alphabet/B',
        #'http://www.wikiart.org/en/Alphabet/C',
        #'http://www.wikiart.org/en/Alphabet/D',
        #'http://www.wikiart.org/en/Alphabet/E',
        #'http://www.wikiart.org/en/Alphabet/F',
        #'http://www.wikiart.org/en/Alphabet/G',
        #'http://www.wikiart.org/en/Alphabet/H',
        #'http://www.wikiart.org/en/Alphabet/I',
        #'http://www.wikiart.org/en/Alphabet/J',
        #'http://www.wikiart.org/en/Alphabet/K',
        #'http://www.wikiart.org/en/Alphabet/L',
        #'http://www.wikiart.org/en/Alphabet/M',
        #'http://www.wikiart.org/en/Alphabet/N',
        #'http://www.wikiart.org/en/Alphabet/O',
        #'http://www.wikiart.org/en/Alphabet/P',
        #'http://www.wikiart.org/en/Alphabet/Q',
        #'http://www.wikiart.org/en/Alphabet/R',
        #'http://www.wikiart.org/en/Alphabet/S',
        #'http://www.wikiart.org/en/Alphabet/T',
        #'http://www.wikiart.org/en/Alphabet/U',
        #'http://www.wikiart.org/en/Alphabet/V',
        #'http://www.wikiart.org/en/Alphabet/W',
        #'http://www.wikiart.org/en/Alphabet/X',
        #'http://www.wikiart.org/en/Alphabet/Y',
        #'http://www.wikiart.org/en/Alphabet/Z',
        #'http://www.wikiart.org/en/Alphabet/3',
    )

    def parse(self, response):
        #conn, cur = DBUtils.get_conn()
        hxs = HtmlXPathSelector(response)

        for sel in hxs.select("//div[@class='pozRel']"):

            #link = "http://www.wikiart.org"
            linkArray = sel.xpath('a/@href').extract()

            link = self._link + linkArray[0]

            #yield Request(url=link, callback=self.parse_artist)
            yield Request(url=link, callback=self.parse_product_pre)
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

    def parse_product_pre(self, response):
        hxs = HtmlXPathSelector(response)
        for sel in hxs.select("//div[@class='pb5']"):
            linkArray = sel.xpath('a/@href').extract()
            link = self._link + linkArray[0]
            yield Request(url=link, callback=self.parse_product)

    def parse_product(self, response):
        product = WikiartProductsItem()
        product['material'] = ''
        product['dimensions'] = ''

        hxs = HtmlXPathSelector(response)

        product['s_url'] = response._url
        product['product_name'] = hxs.xpath("//div[@class='tt30 pb8']/h1/text()").extract()[0]

        product_info = hxs.xpath("//div[@class='ArtistInfo']")

        image_info = product_info.xpath("//a[@id='paintingImage']/@href").extract()[0]
        product['resource_url'] = image_info

        for data_info in product_info.xpath("//div[@class='DataProfileBox']/p"):
            key = data_info.xpath("b/text()").extract()[0]
            if key == 'Material:':
                value = data_info.xpath("text()").extract()[1]
                value = value.replace("\r\n", '')
                product['material'] = product['material'] + value
            elif key == 'Dimensions:':
                value = data_info.xpath("text()").extract()[1]
                value = value.replace("\r\n", '')
                product['dimensions'] = product['dimensions'] + value

        product['create_by'] = hxs.xpath("//a[@itemprop='author']/text()").extract()[0]
        years = product_info.xpath("//span[@itemprop='dateCreated']/text()").extract()
        if len(years) > 0:
            product['create_at'] = years[0]
        else:
            product['create_at'] = 'UnKnown'

        product['product_style'] = product_info.xpath("//span[@itemprop='style']/text()").extract()
        product['product_genre'] = product_info.xpath("//span[@itemprop='genre']/text()").extract()

        return product






