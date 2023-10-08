# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import scrapy


class NewsLink(scrapy.Item):
    id = scrapy.Field()
    link = scrapy.Field()
    crawled = scrapy.Field()


class NewsItem(scrapy.Item):
    id = scrapy.Field()
    url = scrapy.Field()
    headlines = scrapy.Field()
    content = scrapy.Field()
