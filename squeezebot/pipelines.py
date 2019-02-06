# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import html
from datetime import datetime

from w3lib.html import remove_tags


class TrackCleanupPipeline(object):
    def process_item(self, item, spider):
        item["title"] = html.unescape(remove_tags(item.get("title")))
        item["user"] = html.unescape(remove_tags(item.get("user")))
        item["tag"] = html.unescape(remove_tags(item.get("tag", "")))
        item["date"] = datetime.strptime(item.get("date"), "%Y-%m-%dT%H:%M:%S.%fZ")
        try:
            # This field contains the word 'Like' if there are no likes.
            item["likes"] = int(remove_tags(item.get("likes")))
        except ValueError:
            item["likes"] = 0
        item["url"] = remove_tags(item.get("url"))
        return item
