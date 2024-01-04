import scrapy
from ..items import AliexpressItem


class ScraperSpider(scrapy.Spider):
    name = "scraper"
    # allowed_domains = ["www.aliexpress.com"]
    start_urls = ["https://www.aliexpress.com/w/wholesale-watches.html?spm=a2g0o.best.search.0"]

    def parse(self, response):
        items = AliexpressItem()

        div = response.css("div.list--gallery--C2f2tvm.search-item-card-wrapper-gallery")

        for each in div:
            items["name"] = each.css("h1.multi--titleText--nXeOvyr::text").get()
            items["link"] = each.css("a.multi--container--1UZxxHY.cards--card--3PJxwBm.search-card-item::attr(href)").get()

            yield items

