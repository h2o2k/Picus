# Quick unit test to demonstrate unit testing for this application, most of the testing was performed by WBT so this is basic - Andrew

import unittest
import scrapy

from scrapy.crawler import CrawlerProcess
from items import PicusItem
from scrapy.utils.project import get_project_settings

class TestItems(unittest.TestCase):
    def testspider(self):
        item = PicusItem()
        item['img'] = 'https://i.imgur.com/grokIvc.png'
        item['title'] = 'This is a test'
        item['url'] = 'This is a test'
        item['blurb'] = 'This is a test'
        item['uploadtime'] = 'This is a test'
        item['author'] = 'Testing'

if __name__ == '__main__':
    unittest.main()
