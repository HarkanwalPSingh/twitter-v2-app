from typing import Any
from pathlib import Path

import scrapy
from scrapy.http import Response
from scrapy.loader import ItemLoader

from scrappers.items import NewsItem


class NewsSpider(scrapy.Spider):
    name = "news-spider"
    start_urls = [
        "https://www.hindustantimes.com/cities/bengaluru-news"
    ]
    allowed_domains = [
        "hindustantimes.com"
    ]

    def parse(self, response: Response):
        mainContainer = response.css("section.mainContainer")
        article_anchors = mainContainer.css("div.cartHolder")
        # anchors = article_anchors.css("h3.hdg3 a::attr(href)").getall()

        article_page_links = article_anchors.css("h3.hdg3 a")

        yield from response.follow_all(article_page_links, self.parse_news)

        # filename = "article-anchors.txt"
        # Path(filename).write_text("\n".join(anchors))
    
    def parse_news(self, response):
        def extract_with_css(query):
            return response.css(query).get(default="").strip()
        
        mainContainer = response.css("section.mainContainer")

        loader = ItemLoader(NewsItem(), response=response)

        loader.add_value("url", response.url)
        loader.add_css("headlines", "section.mainContainer div#dataHolder h1::text")
        loader.add_css("content", "section.mainContainer p::text")

        yield loader.load_item()
        
        # yield {
        #     "headlines": mainContainer.css("div#dataHolder h1::text").get(),
        #     "text" : mainContainer.css("p::text").getall()
        # }


# scrapy shell 'https://www.hindustantimes.com/cities/bengaluru-news'

# mainContainer = response.css("section.mainContainer")
# article_anchor = mainContainer.css("div.cartHolder h3.hdg3 a")[0]
# article_link = article_anchor.css("a::attr(href)").get()


# ## For getting all article links
# article_anchors = mainContainer.css("div.cartHolder")
# article_anchors.css("h3.hdg3 a::attr(href)").getall()
