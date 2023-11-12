# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import scrapy
from itemloaders.processors import MapCompose, Join

# Not needed I think
class NewsLink(scrapy.Item):
    id = scrapy.Field()
    link = scrapy.Field()
    crawled = scrapy.Field()


class NewsItem(scrapy.Item):
    url = scrapy.Field()
    headlines = scrapy.Field()
    content = scrapy.Field(
        output_processor = Join("")
    )
