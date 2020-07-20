# Picus
<!-- information document for the project - Andrew -->
Final Year Project for UU 2020.

Libraries used:
1. Scrapy - Crawls the websites for our project
2. MongoDB - Database server for storing scraped content
3. PyMongo - Allows Scrapy, MongoDB and FLASK to interact
4. Flask - Framework which can create web dev applications
5. HTML, CSS, JavaScript & Bootstrap - Formatting webpages
6. Scrapy-do - schedules scrapy to run on a set schedule
7. flask_paginate - Lets us set up pagination on the website

General creation guide for future additions:
1. Create the scrapy project
2. Create items.py to store scraped items
3. Create your spiders which can then crawl websites
4. Create the pipeline that connects the data from crawled websites and inserts them into MongoDB
5. Retrieve information via Flask
6. Create the templates and routes for Flask

Running:
1. Run mangod to start the database service and run compass for a GUI version of the database
2. Run spiders individually or run the entire project via "python app.py"
3. Check compass to ensure that data is entering into the database
4. Run flask individually or ignore if you have ran via "python app.py"
5. Navigate to 'localhost:5000' to view the website

Code references:
Bootstrap themes and flask layouts have been taken from:
https://github.com/CoreyMSchafer/code_snippets/tree/master/Python/Flask_Blog
