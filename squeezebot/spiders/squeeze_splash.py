# -*- coding: utf-8 -*-
import os

import scrapy
from scrapy.exceptions import CloseSpider
from scrapy_splash import SplashRequest


class SqueezeSplashSpider(scrapy.Spider):
    name = "squeeze-splash"
    allowed_domains = ["soundcloud.com"]
    start_urls = [
        "https://soundcloud.com/search/sounds?q=accordion&filter.created_at=last_week"
    ]

    def __init__(self, target_count=-1, *args, **kwargs):
        self.target_count = int(target_count)
        super().__init__(*args, **kwargs)

    def infinite_scroll_script_path(self):
        """Returns the path to the infinite scroll Lua script."""
        dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        filepath = os.path.join(dir, "lua", "infinite_scroll.lua")
        return filepath

    def start_requests(self):
        try:
            with open(self.infinite_scroll_script_path(), "r") as file:
                script = file.read()

            for url in self.start_urls:
                yield SplashRequest(
                    url,
                    self.parse,
                    endpoint="execute",
                    args={
                        "lua_source": script,
                        "wait": 5,
                        "timeout": 600,
                        "target_count": self.target_count,
                    },
                )
        except:
            raise CloseSpider("Could not load Lua script.")

    def parse(self, response):
        for item in response.css(".searchItem")[: self.target_count]:
            yield {
                "user": item.css(".soundTitle__usernameText::text").get(),
                "title": item.css(".soundTitle__title span::text").get(),
                "tag": item.css(".soundTitle__tagContent::text").get(),
                "popularity": item.css(".sc-button-like::text").get(),
                "link": item.css(".soundTitle__title::attr(href)").get(),
            }
