## The &rsquo;Zine

Unofficial python api of [The &rsquo;Zine](http://thezine.biz)

| Build Status | Version |Test Coverage |
| ------------ | ------- | ------------ |
| [![Build Status](https://travis-ci.org/voidabhi/TheZineAPI.svg)](https://travis-ci.org/voidabhi/TheZineAPI)|[![Latest Version](https://img.shields.io/pypi/v/TheZine.svg)](https://pypi.python.org/pypi/TheZine/) | [![Coverage Status](https://img.shields.io/coveralls/voidabhi/TheZineAPI.svg)](https://coveralls.io/r/voidabhi/TheZineAPI?branch=master)|

### Installation


### Method 1 - Pip

```bash
$ pip install TheZine
````

### Method 2 - Build from source

```bash
$ git clone git@github.com:voidabhi/TheZine.git
$ cd TheZine
$ python setup.py install
```

### Dependencies

The library is built with `Requests` and `BeautifulSoup`.

### Built By

`Abhijeet Mohan` - `void.aby@gmail.com`

<a href="https://plus.google.com/104070882148677917719/about">
  <img alt="Follow me on Google+"
       src="http://data.pkmmte.com/temp/social_google_plus_logo.png" />
</a>

### Usage

	# importing the library
    from tz import TZ
	
	# instantiating TZ object
    tz = TZ()

    # fetch all the articles of an issue in a dict
    for article in tz.get_articles(issue='2'):
        print(article['title'])
		
### Contribute

Feel free to send pull requests!
		
### LICENSE

```

The MIT License (MIT)

Copyright (c) 2014 Abhijeet Mohan - https://github.com/voidabhi/TheZineAPI

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

```
