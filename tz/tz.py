
#!/usr/bin/env python

"""
The Zine API
Unofficial Python API for The Zine

@author Abhijeet Mohan
@email void.aby@gmail.com
"""


import requests
from bs4 import BeautifulSoup

from constants import BASE_URL, INTERVAL_BETWEEN_REQUESTS
from utils import get_soup

class TZ(object):
    """
    The class that parses the TZ page, and builds up all articles
    """
	
	
    def __init__(self):
        self.more = ''
		
    def _get_zipped_articles(self, soup,issue):
        """
        Returns all 'ul' tag rows as a list of tuples. Each tuple is for
        a single article.
        """	
	issues = soup.find_all('ul')
		
		# validating and assigning default value for issue
	if not type(issue) is int or issue < 0 :
		issue = 1
	if issue > len(issues):
		issue = len(issues)		
		
		
	articles = issues[len(issues)-issue].find_all('a') #considering latest article is last element 
	mArticles = []
	for article in articles:
		mArticle = {}
		mArticle['link'] = article.get('href')
		mArticle['title'] = article.find('li').contents[0].strip()
		mArticle['author'] = article.find('span').contents[0].encode('utf8')
		mArticles.append(mArticle)
			
	return mArticles
	
	
	def _build_article(self, articles_dict):
		pass
		
    def get_articles(self, issue='', limit=10):
        """
        Yields a list of articles from the given issue.

        'limit' is the number of articles required from the given issue.
        Defaults to all
        """	
        if limit == None or limit < 1 or limit > 10:
            limit = 10 # at least 10 articles

	articles_found = 0
		
        #while articles_found < limit:
	soup = get_soup() # get soup of all articles 
	all_articles = self._get_zipped_articles(soup,issue=issue)
	return all_articles
            #articles = self._build_article(all_articles) # get a list of articles of current issue

    """
	 for article in articles:
        yield article
                articles_found += 1

                # if enough articles found, return
                if articles_found == limit:
                    return	
					
	"""		

class Article(object):
	pass

class Author(object):
	pass
		

					
if __name__ == '__main__':
	print TZ().get_articles()
