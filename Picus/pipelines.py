# -*- coding: utf-8 -*-
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# Inserting data from the crawlers into our database
# Scraped data -> Items.py containers -> Pipelines -> MongoDB database <- We will be using this method - Andrew

import pymongo

from scrapy.exceptions import DropItem

class PicusPipeline(object):

    collection_name = 'Articles'

    def __init__(self, mongo_uri, mongo_db): # Starting our connection to the mongoDB server
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.titles_seen = set()

    @classmethod
    def from_crawler(cls, crawler): # Pulls in information from scrapy settings.py
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'items')
        )

    def open_spider(self, spider): # Initializing the spiders and opening a db connection
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider): # Cleaning up when the spider is finshed crawling
        self.client.close()

    def process_item(self, item, spider): # How to handle each of the posts we scraped
        # if item['title'] in self.titles_seen: # This is a simple check which can only parse for items that have been crawled, will need unique title to prevent further additions to DB. Not working and will drop all titles if even one character is similar
        #     raise DropItem("Duplicate item found: %s" % item)
        # else:
            self.titles_seen.add(item['title'])
            self.db[self.collection_name].create_index([("title", pymongo.TEXT)], unique=True) # This creates a unique index on the title that prevents duplicate data from being entered into the database
            self.db[self.collection_name].insert(dict(item))
            return item
