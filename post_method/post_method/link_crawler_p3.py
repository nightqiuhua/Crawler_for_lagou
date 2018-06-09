import re 
import datetime 
import time 
from downloader_requests_p3 import Downloader
from mogon_cache import MongoCache
from scrape_callback2_p3 import ScrapeCallback
import lxml.html
import json
import itertools

def link_crawler(seed_url,link_regx=None,delay=5,max_depth=2,max_urls=-1,user_agent=None,proxies=None,num_retries=1,scrape_callback=None,cache=None):
	D = Downloader(delay=delay,user_agent=user_agent,proxies=proxies,num_tries=num_retries,cache=cache)
	for page in range(1,31):
		url = seed_url
		params = {'first':'true','pn':str(page),'kd':'Python'}
		print('page=',page)
		try:
			html = D(url,data=params)
		except Exception as e:
			raise e
		else:
			if scrape_callback:
				scrape_callback.__call__(html)

	

seed_url = 'https://www.lagou.com/jobs/positionAjax.json'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
link_crawler(seed_url=seed_url,user_agent=user_agent,scrape_callback=ScrapeCallback(),cache = MongoCache())