The &rsquo;Zine
===============

Unofficial python api for the blog [The &rsquo;Zine](http://thezine.biz)

| Build Status | Version |
| ------------ | ------------- 
| [![Build Status](https://travis-ci.org/karan/HackerNewsAPI.png?branch=master)](https://travis-ci.org/karan/HackerNewsAPI)|[![Latest Version](https://pypip.in/v/TheZine/badge.png)](https://pypi.python.org/pypi/TheZine/) 

Installation
============

    $ pip install TheZine

Dependencies
============

The library is built on top of Requests and BeautifulSoup modules.

Features
==========

Comming Soon!

Usage
==========


    from tz import TZ

    tz = TZ()

    # fetch all the articles of an issue in a dict
    for article in tz.get_articles(issue='2'):
        print(article['title'])

