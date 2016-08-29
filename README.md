#Scrapy module - Web Crawling


## Introduction
Scrapy is an application framework for crawling web sites and extracting structured data which can be used for a wide range of useful applications, like data mining, information processing or historical archival.

Even though Scrapy was originally designed for web scraping, it can also be used to extract data using APIs (such as Amazon Associates Web Services) or as a general purpose web crawler.

## Architecture

![Architecture](http://doc.scrapy.org/en/latest/_images/scrapy_architecture.png "Scrapy Architecture")

[Visit here for more](http://doc.scrapy.org/en/latest/topics/architecture.html#architecture-overview)
## Project Structure
tutorial/
    scrapy.cfg            # deploy configuration file

    tutorial/             # project's Python module, you'll import your code from here
        __init__.py

        items.py          # project items file

        pipelines.py      # project pipelines file

        settings.py       # project settings file

        spiders/          # a directory where you'll later put your spiders
            __init__.py
        

## Features

- Built-in support for selecting and extracting data from HTML/XML sources using extended CSS selectors and XPath expressions, with helper methods to extract using regular expressions.
- An interactive shell console (IPython aware) for trying out the CSS and XPath expressions to scrape data, very useful when writing or debugging your spiders.
- Built-in support for generating feed exports in multiple formats (JSON, CSV, XML) and storing them in multiple backends (FTP, S3, local filesystem)
- Robust encoding support and auto-detection, for dealing with foreign, non-standard and broken encoding declarations.
- Strong extensibility support, allowing you to plug in your own functionality using signals and a well-defined API (middlewares, extensions, and pipelines).
- Wide range of built-in extensions and middlewares for handling:
  * cookies and session handling
  * HTTP features like compression, authentication, caching
  * user-agent spoofing
  * robots.txt
  * crawl depth restriction

- A Telnet console for hooking into a Python console running inside your Scrapy process, to introspect and debug your crawler
Plus other goodies like reusable spiders to crawl sites from Sitemaps and XML/CSV feeds, a media pipeline for automatically downloading images (or any other media) associated with the scraped items, a caching DNS resolver, and much more
