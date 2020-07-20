# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

# Here are the spiders that are designed for crawling various news websites - Andrew

import scrapy

from scrapy import Spider
from datetime import datetime # Needed as BBC does not include a standard date time functionality across the website
from scrapy.selector import Selector
from Picus.items import PicusItem # Importing storage containers for the data we plan to scrape

class BBCSpider(scrapy.Spider): # Inherits features from the pre-existing scrapy spider class
    name = "BBC" # Defines the name of the crawler when running in CMD
    allowed_domains = ["www.bbc.co.uk"] # Limit URL's that our spider is allowed to crawl
    start_urls = ["https://www.bbc.co.uk/news/technology"] # Starting destination for our web crawler

    def parse(self, response): # Crawling using CSS as xpaths are very confusing on the BBC news website
        articles = Selector(response).css('.gs-c-promo') # Pointing our webcrawler in the right direction as we only want a certain section of the webpage - can be found via inspect element in Chrome and Firefox
        for article in articles: # Loop that goes throught each of the articles found in search of relevant items
            item = PicusItem()
            append = ['https://www.bbc.co.uk'] # Needed to complete the URL as it doesn't extract the full URL
            uploadtime = '{0:%m-%d-%y}'.format(datetime.now())

            item['img'] = 'https://i.imgur.com/grokIvc.png' # Images are not loading due to lazyloading a script which only loads images as they come into display so instead we are using a blank default, need scrapyjs or seleniu
            item['title'] = article.css('h3.gs-c-promo-heading__title::text').extract_first(default='This article did not include a title.') # CSS selectors that are grabbing relevant data for each our items
            item['url'] = ''.join(append + article.css('a.gs-c-promo-heading::attr(href)').extract())
            item['blurb'] = article.css('p.gs-c-promo-summary::text').extract_first(default='This article did not include a blurb.')
            item['uploadtime'] = uploadtime # BBC does not use a format that is accepted for date time which we can format later, instead we will have to set the uploadtime equal to todays date
            item['author'] = 'BBC Technology News' # BBC news articles do not contain an author, instead we will use the section
            yield item # Uses yield instead of return as scrapy generates the data behind the scenes

class BBCLocalSpider(scrapy.Spider): # Spider for crawling the local BBC news
    name = "BBCLocal"
    allowed_domains = ["www.bbc.co.uk"]
    start_urls = ["https://www.bbc.co.uk/news/northern_ireland"]

    def parse(self, response):
        articles = Selector(response).css('.gs-c-promo')
        for article in articles:
            item = PicusItem()
            append = ['https://www.bbc.co.uk']
            uploadtime = '{0:%m-%d-%y}'.format(datetime.now())

            item['img'] = 'https://i.imgur.com/grokIvc.png'
            item['title'] = article.css('h3.gs-c-promo-heading__title::text').extract_first(default='This article did not include a title.')
            item['url'] = ''.join(append + article.css('a.gs-c-promo-heading::attr(href)').extract())
            item['blurb'] = article.css('p.gs-c-promo-summary::text').extract_first(default='This article did not include a blurb.')
            item['uploadtime'] = uploadtime
            item['author'] = 'BBC Local News'
            yield item

class BBCGlobalSpider(scrapy.Spider): # Spider for crawling the world BBC news
    name = "BBCGlobal"
    allowed_domains = ["www.bbc.co.uk"]
    start_urls = ["https://www.bbc.co.uk/news/world"]

    def parse(self, response):
        articles = Selector(response).css('.gs-c-promo')
        for article in articles:
            item = PicusItem()
            append = ['https://www.bbc.co.uk']
            uploadtime = '{0:%m-%d-%y}'.format(datetime.now())

            item['img'] = 'https://i.imgur.com/grokIvc.png'
            item['title'] = article.css('h3.gs-c-promo-heading__title::text').extract_first(default='This article did not include a title.')
            item['url'] = ''.join(append + article.css('a.gs-c-promo-heading::attr(href)').extract())
            item['blurb'] = article.css('p.gs-c-promo-summary::text').extract_first(default='This article did not include a blurb.')
            item['uploadtime'] = uploadtime
            item['author'] = 'BBC Global News'
            yield item

class BBCScienceSpider(scrapy.Spider): # Spider for crawling the science BBC news
    name = "BBCScience"
    allowed_domains = ["www.bbc.co.uk"]
    start_urls = ["https://www.bbc.co.uk/news/science_and_environment"]

    def parse(self, response):
        articles = Selector(response).css('.gs-c-promo')
        for article in articles:
            item = PicusItem()
            append = ['https://www.bbc.co.uk']
            uploadtime = '{0:%m-%d-%y}'.format(datetime.now())

            item['img'] = 'https://i.imgur.com/grokIvc.png'
            item['title'] = article.css('h3.gs-c-promo-heading__title::text').extract_first(default='This article did not include a title.')
            item['url'] = ''.join(append + article.css('a.gs-c-promo-heading::attr(href)').extract())
            item['blurb'] = article.css('p.gs-c-promo-summary::text').extract_first(default='This article did not include a blurb.')
            item['uploadtime'] = uploadtime
            item['author'] = 'BBC Science News'
            yield item

class BBCEntertainmentSpider(scrapy.Spider): # Spider for crawling the entertainment BBC news
    name = "BBCEntertainment"
    allowed_domains = ["www.bbc.co.uk"]
    start_urls = ["https://www.bbc.co.uk/news/entertainment_and_arts"]

    def parse(self, response):
        articles = Selector(response).css('.gs-c-promo')
        for article in articles:
            item = PicusItem()
            append = ['https://www.bbc.co.uk']
            uploadtime = '{0:%m-%d-%y}'.format(datetime.now())

            item['img'] = 'https://i.imgur.com/grokIvc.png'
            item['title'] = article.css('h3.gs-c-promo-heading__title::text').extract_first(default='This article did not include a title.')
            item['url'] = ''.join(append + article.css('a.gs-c-promo-heading::attr(href)').extract())
            item['blurb'] = article.css('p.gs-c-promo-summary::text').extract_first(default='This article did not include a blurb.')
            item['uploadtime'] = uploadtime
            item['author'] = 'BBC Entertainment News'
            yield item

class gHacksSpider(scrapy.Spider): # Spider for crawling the gHacks website
    name = "gHacks"
    page_number = 2
    allowed_domains = ["www.ghacks.net"]
    start_urls = ["https://www.ghacks.net/"]

    def parse(self, response):
        articles = Selector(response).css('.post-list')
        for article in articles:
            item = PicusItem()
            uploadtime = '{0:%m-%d-%y}'.format(datetime.now())

            item['img'] = article.css('img.attachment-thumbnail::attr(src)').extract_first()
            item['title'] = article.css('a.link::text').extract_first(default='This article did not include a title.')
            item['url'] = article.css('a.link::attr(href)').extract_first()
            item['blurb'] = article.css('p::text').extract_first(default='This article did not include a blurb.')
            item['uploadtime'] = uploadtime # Uploadtime cannot be grabbed again from this webpage
            item['author'] =  'gHacks'
            yield item

        next_page = 'https://www.ghacks.net/page/'+ str(gHacksSpider.page_number) +'/' # Appending to the URL of gHacks allows us to crawl 5 pages deep
        if gHacksSpider.page_number <=10:
            gHacksSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)

class theGuardianSpider(scrapy.Spider): # Was going to be used for URL splitting hower reddit is used now instead. This website has a lot of issues with consistant storage for titles, links, names etc
    name = "theGuardian"
    allowed_domains = ["www.theguardian.com"]
    start_urls = ["https://www.theguardian.com/uk/technology/"]

    def parse(self, response):
        articles = Selector(response).css('.fc-container')
        for article in articles:
            item = PicusItem()
            uploadtime = '{0:%m-%d-%y}'.format(datetime.now())

            item['img'] = 'https://i.imgur.com/grokIvc.png' # Images can not be grabbed due to the non-uniform classes that being used to store images
            item['title'] = article.css('a.js-headline-text::text').extract_first(default='News article from The Guardian')
            item['url'] = article.css('a.fc-item__link::attr(href)').extract_first(default='https://www.theguardian.com/uk/technology')
            item['blurb'] = 'This article did not include a blurb.' # theGuardian does not have blurbs and instead only has the title name
            item['uploadtime'] = uploadtime # Uploadtime cannot be grabbed again from this webpage as it does not exist
            item['author'] =  'Guardian technology'
            yield item

class theGuardianLocalSpider(scrapy.Spider):
    name = "theGuardianLocal"
    allowed_domains = ["www.theguardian.com"]
    start_urls = ["https://www.theguardian.com/uk-news"]

    def parse(self, response):
        articles = Selector(response).css('.fc-container')
        for article in articles:
            item = PicusItem()
            uploadtime = '{0:%m-%d-%y}'.format(datetime.now())

            item['img'] = 'https://i.imgur.com/grokIvc.png'
            item['title'] = article.css('a.js-headline-text::text').extract_first(default='News article from The Guardian')
            item['url'] = article.css('a.fc-item__link::attr(href)').extract_first(default='https://www.theguardian.com/uk-news')
            item['blurb'] = 'This article did not include a blurb.'
            item['uploadtime'] = uploadtime
            item['author'] =  'Guardian local'
            yield item

class theGuardianWorldSpider(scrapy.Spider):
    name = "theGuardianWorld"
    allowed_domains = ["www.theguardian.com"]
    start_urls = ["https://www.theguardian.com/world"]

    def parse(self, response):
        articles = Selector(response).css('.fc-container')
        for article in articles:
            item = PicusItem()
            uploadtime = '{0:%m-%d-%y}'.format(datetime.now())

            item['img'] = 'https://i.imgur.com/grokIvc.png'
            item['title'] = article.css('a.js-headline-text::text').extract_first(default='News article from The Guardian')
            item['url'] = article.css('a.fc-item__link::attr(href)').extract_first(default='https://www.theguardian.com/world')
            item['blurb'] = 'This article did not include a blurb.'
            item['uploadtime'] = uploadtime #
            item['author'] =  'Guardian world'
            yield item

class theGuardianScienceSpider(scrapy.Spider):
    name = "theGuardianScience"
    allowed_domains = ["www.theguardian.com"]
    start_urls = ["https://www.theguardian.com/uk/environment"]

    def parse(self, response):
        articles = Selector(response).css('.fc-container')
        for article in articles:
            item = PicusItem()
            uploadtime = '{0:%m-%d-%y}'.format(datetime.now())

            item['img'] = 'https://i.imgur.com/grokIvc.png'
            item['title'] = article.css('a.js-headline-text::text').extract_first(default='News article from The Guardian')
            item['url'] = article.css('a.fc-item__link::attr(href)').extract_first(default='https://www.theguardian.com/uk/environment')
            item['blurb'] = 'This article did not include a blurb.'
            item['uploadtime'] = uploadtime
            item['author'] =  'Guardian science'
            yield item

class theGuardianEntertainmentSpider(scrapy.Spider):
    name = "theGuardianEntertainment"
    allowed_domains = ["www.theguardian.com"]
    start_urls = ["https://www.theguardian.com/uk/culture"]

    def parse(self, response):
        articles = Selector(response).css('.fc-container')
        for article in articles:
            item = PicusItem()
            uploadtime = '{0:%m-%d-%y}'.format(datetime.now())

            item['img'] = 'https://i.imgur.com/grokIvc.png'
            item['title'] = article.css('a.js-headline-text::text').extract_first(default='News article from The Guardian')
            item['url'] = article.css('a.fc-item__link::attr(href)').extract_first(default='https://www.theguardian.com/uk/culture')
            item['blurb'] = 'This article did not include a blurb.'
            item['uploadtime'] = uploadtime
            item['author'] =  'Guardian entertainment'
            yield item

class redditSpider(scrapy.Spider):
    name = "reddit"
    allowed_domains = ["www.reddit.com"]
    start_urls = ["https://old.reddit.com/r/popular/"]

    def parse(self, response):
        articles = Selector(response).css('div.thing')
        for article in articles:
            item = PicusItem()
            uploadtime = '{0:%m-%d-%y}'.format(datetime.now())

            item['img'] = 'https://i.imgur.com/grokIvc.png'
            item['title'] = article.css('a.title::text').extract_first(default='This article did not include a title.')
            item['url'] = article.css('a.title::attr(href)').extract_first()
            item['blurb'] = 'This article did not include a blurb.'
            item['uploadtime'] = uploadtime
            item['author'] =  'Reddit'
            yield item

class redditLocalSpider(scrapy.Spider):
    name = "redditLocal"
    allowed_domains = ["www.reddit.com"]
    start_urls = ["https://old.reddit.com/r/unitedkingdom/"]

    def parse(self, response):
        articles = Selector(response).css('div.thing')
        for article in articles:
            item = PicusItem()
            uploadtime = '{0:%m-%d-%y}'.format(datetime.now())

            item['img'] = 'https://i.imgur.com/grokIvc.png'
            item['title'] = article.css('a.title::text').extract_first(default='This article did not include a title.')
            item['url'] = article.css('a.title::attr(href)').extract_first()
            item['blurb'] = 'This article did not include a blurb.'
            item['uploadtime'] = uploadtime
            item['author'] =  'Reddit local'
            yield item

class redditGlobalSpider(scrapy.Spider):
    name = "redditGlobal"
    allowed_domains = ["www.reddit.com"]
    start_urls = ["https://old.reddit.com/r/news/"]

    def parse(self, response):
        articles = Selector(response).css('div.thing')
        for article in articles:
            item = PicusItem()
            uploadtime = '{0:%m-%d-%y}'.format(datetime.now())

            item['img'] = 'https://i.imgur.com/grokIvc.png'
            item['title'] = article.css('a.title::text').extract_first(default='This article did not include a title.')
            item['url'] = article.css('a.title::attr(href)').extract_first()
            item['blurb'] = 'This article did not include a blurb.'
            item['uploadtime'] = uploadtime
            item['author'] =  'Reddit global'
            yield item

class redditScienceSpider(scrapy.Spider):
    name = "redditScience"
    allowed_domains = ["www.reddit.com"]
    start_urls = ["https://old.reddit.com/r/science/"]

    def parse(self, response):
        articles = Selector(response).css('div.thing')
        for article in articles:
            item = PicusItem()
            uploadtime = '{0:%m-%d-%y}'.format(datetime.now())

            item['img'] = 'https://i.imgur.com/grokIvc.png'
            item['title'] = article.css('a.title::text').extract_first(default='This article did not include a title.')
            item['url'] = article.css('a.title::attr(href)').extract_first()
            item['blurb'] = 'This article did not include a blurb.'
            item['uploadtime'] = uploadtime
            item['author'] =  'Reddit science'
            yield item

class redditEntertainmentSpider(scrapy.Spider):
    name = "redditEntertainment"
    allowed_domains = ["www.reddit.com"]
    start_urls = ["https://old.reddit.com/r/movies/"]

    def parse(self, response):
        articles = Selector(response).css('div.thing')
        for article in articles:
            item = PicusItem()
            uploadtime = '{0:%m-%d-%y}'.format(datetime.now())

            item['img'] = 'https://i.imgur.com/grokIvc.png'
            item['title'] = article.css('a.title::text').extract_first(default='This article did not include a title.')
            item['url'] = article.css('a.title::attr(href)').extract_first()
            item['blurb'] = 'This article did not include a blurb.'
            item['uploadtime'] = uploadtime
            item['author'] =  'Reddit entertainment'
            yield item

class wiredSpider(scrapy.Spider):
    name = "wired"
    allowed_domains = ["www.wired.co.uk"]
    start_urls = ["https://www.wired.co.uk/topic/technology"]

    def parse(self, response):
        articles = Selector(response).css('.c-card')
        for article in articles:
            item = PicusItem()
            uploadtime = '{0:%m-%d-%y}'.format(datetime.now())
            append = ['https://www.wired.co.uk'] # Needed to complete the URL as it doesn't extract the full URL

            item['img'] = 'https://i.imgur.com/grokIvc.png'
            item['title'] = article.css('a.c-card__link::text').extract_first(default='This article did not include a title.')
            item['url'] = ''.join(append + article.css('a.c-card__link::attr(href)').extract())
            item['blurb'] = 'This article did not include a blurb.'
            item['uploadtime'] = uploadtime # Uploadtime cannot be grabbed again from this webpage
            item['author'] =  article.css('span.c-card__byline-name::text').extract_first()
            yield item

class wiredScienceSpider(scrapy.Spider):
    name = "wiredScience"
    allowed_domains = ["www.wired.co.uk"]
    start_urls = ["https://www.wired.co.uk/topic/science"]

    def parse(self, response):
        articles = Selector(response).css('.c-card')
        for article in articles:
            item = PicusItem()
            uploadtime = '{0:%m-%d-%y}'.format(datetime.now())
            append = ['https://www.wired.co.uk']

            item['img'] = 'https://i.imgur.com/grokIvc.png'
            item['title'] = article.css('a.c-card__link::text').extract_first(default='This article did not include a title.')
            item['url'] = ''.join(append + article.css('a.c-card__link::attr(href)').extract())
            item['blurb'] = 'This article did not include a blurb.'
            item['uploadtime'] = uploadtime
            item['author'] =  article.css('span.c-card__byline-name::text').extract_first()
            yield item

class wiredEntertainmentSpider(scrapy.Spider):
    name = "wiredEntertainmentSpider"
    allowed_domains = ["www.wired.co.uk"]
    start_urls = ["https://www.wired.co.uk/topic/culture"]

    def parse(self, response):
        articles = Selector(response).css('.c-card')
        for article in articles:
            item = PicusItem()
            uploadtime = '{0:%m-%d-%y}'.format(datetime.now())
            append = ['https://www.wired.co.uk']

            item['img'] = 'https://i.imgur.com/grokIvc.png'
            item['title'] = article.css('a.c-card__link::text').extract_first(default='This article did not include a title.')
            item['url'] = ''.join(append + article.css('a.c-card__link::attr(href)').extract())
            item['blurb'] = 'This article did not include a blurb.'
            item['uploadtime'] = uploadtime
            item['author'] =  article.css('span.c-card__byline-name::text').extract_first()
            yield item
