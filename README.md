The &rsquo;Zine
===============

Unofficial python api for the blog [The &rsquo;Zine](http://thezine.biz)

| Build Status | Version | Coverage |
| ------------ | ------- | -------- |
| [![Build Status](https://travis-ci.org/voidabhi/TheZineAPI.svg)](https://travis-ci.org/voidabhi/TheZineAPI)|[![Latest Version](https://pypip.in/v/TheZine/badge.png)](https://pypi.python.org/pypi/TheZine/) 

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
		
Contribute
==========

Furiously waiting for pull requests.
		
LICENSE
==========

The MIT License (MIT)

Copyright (c) 2014 Abhijeet Mohan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

