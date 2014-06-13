

from os import path
import sys
import unittest

from test_utils import get_content , PRESETS_DIR
from tz import TZ , Article

import httpretty

class TestGetArticles(unittest.TestCase):
	
	def setUp(self):
		httpretty.HTTPretty.enable()
		httpretty.register_uri(httpretty.HTTPretty.GET,'http://thezine.biz/issue-4/bubble',body=get_content('article.html'))
	
		self.tz = TZ()
		self.article = Article.fromLink('issue-4/bubble')
	
	def test_article_from_link_constructor(self):
		"""
			Testing returned articles
		"""
		self.assertEqual(self.article.id,'issue-4-bubble')
		self.assertEqual(self.article.title,'Just Bubble Stuff.')
		self.assertEqual(self.article.tagline,'On Economics.')
		self.assertEqual(self.article.body,"""
		<div class="inner">
		<p>On 4 July 1999, the Clarks family was rejoicing with almost all of America (well, or so it seemed, with a thousand people in a lavish park) in a party thrown by Anonymous.com. It was a dot-com firm and that was enough for all the invitees to not only suit up, but also invest their life savings in the ‘future of the world’. It all started around 1995, when the number of internet users skyrocketed and hence the idea of converting them into customers was conceived by many (if not all). These companies came to be referred as ‘dot-coms’ and soon that’s all it took to have investors- a ‘.com’ on your visiting card. The entire thought process of businessmen seemed to be revolutionised and the thrust was on getting ‘big fast’ by building up consumer base and brand awareness to earn profits later.</p>
		<p>Building up goodwill for a business that was not even planned, was exactly what was happening. The idea was to make internet a business platform which would not only be a tool for business like for management purposes, but also to actually make internet a business- online shopping being the cornerstone.</p>
		<p>This business model relied more on networking than earning profits and hence they operated at a sustained net loss. These companies put the bull racers of Tomatina festival in Spain to shame when it came to daring practices to promote ‘future business’.</p>
		<p>The entire idea of ’getting big’ seemed to be supported by low interest rates in 1998-99 and engendered a bubble built up of technology heavy NASDAQ Composite peaked at 5,048.62 on 10 march, 2010- almost double its previous year’s value.</p>
		<p>The term ‘bubble burst’ is probably the only word in the entire lexicon, that has obliterated world economies and shattered most hopes. A theory that security prices rise above their true value and will continue to do so until prices go into freefall and the bubble bursts.</p>
		<p>The conclusions of law, which declared Microsoft a monopoly, were widely expected in the weeks before their release on April 3. The following day, April 4, the NASDAQ fell from 4,283 points to 3,649 and rebounded back to 4,223, forming an intraday chart that looked like a stretched V. At the time, this represented the most volatile day in the history of the NASDAQ and the bubble was pricked. By 2001, the bubble was deflating at full speed. A majority of the dot-coms ceased trading after burning through their venture capital, many having never made a profit. Investors often referred to these failed dot-coms as "dot-bombs". Well, they were nothing else.</p>
		<p>Retrospecting the whole incident, the concept of ‘think big’ cannot be thrown into oblivion.  It was, admittedly, a brilliant business idea but, it was anachronous, for- the public was still online-o-phobic engendered by the insecurity of online transactions and inability to trust online vendors. Amazon, Ebay, Flipkart, etc. are successful models of this very business idea and hence prove my point adequately. Also, the urge of the American Upper Middle class to invest was driven by social status built up more than the practical profitability of the business which hampered the country’s economy, which points out to the necessity of contemplating ‘new ideas’ a little wisely in order to prevent such tsunamis of bubble.</p>
		<p>Nevertheless, the Clarks, the richest on Terimond Street, New York were ruined (read ultra-bankrupt, if that’s a word). Unfortunately for many companies and investors, the growth of the tech sector proved to be an illusion and courts were soon filled by files of cases against dot-coms and their ‘daring’ business practices and closure of fancy dot-coms seemed inevitable. The issues of the bubble were also compounded by outside factors, like a rise in outsourcing that led to widespread unemployment among computer developers and programmers. The consequences were prodigious. The IT bubble had burst, and- well, it was not a bubble bath anymore.</p>
		</div>		
		""".strip())
	
	def tearDown(self):
		httpretty.HTTPretty.disable()
	

if __name__ == '__main__':
	unittest.main()
