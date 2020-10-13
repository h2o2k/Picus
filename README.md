# Picus
> Web based content aggregator written in Python.

![](Header.png)

## Requirements
1. Scrapy - Web crawler written in Python
2. MongoDB - Database for storing scraped content
3. PyMongo - Scrapy, MongoDB and Flask to interact
4. Flask - Framework to create web applications
5. HTML, CSS, JavaScript & Bootstrap - Webpage formatting
6. Scrapy-do - Scheduling Scrapy to run on at set intervals
7. flask_paginate - Pagination on the Flask application

## Installation
1. Clone repository and navigate into the directory via a CLI

## Running:
1. Run mangod to start the database service or run MongoDB Compass for a GUI version
2. Run spiders individually or run the entire project via "python app.py"
3. Check compass to ensure that data is entering into the database
4. Run flask individually via "routes.py" or ignore if you have ran via "python app.py"
5. Navigate to 'localhost:5000' to view the application

## Future additions
1. Create the scrapy project
2. Create items.py to store scraped items
3. Create your spiders which can then crawl websites
4. Create the pipeline that connects the data from crawled websites and inserts them into MongoDB
5. Retrieve information via Flask
6. Create the templates and routes for Flask

## Contributing
1. Fork it (<https://github.com/yourname/yourproject/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

## References
Bootstrap themes and flask layouts have been taken from:
https://github.com/CoreyMSchafer/code_snippets/tree/master/Python/Flask_Blog
