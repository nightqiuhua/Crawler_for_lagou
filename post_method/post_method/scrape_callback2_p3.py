import lxml.html 
from pymongo import MongoClient,errors
from datetime import datetime,timedelta
import pymongo
import requests#遇到抓取script变量时，使用requests抓取网页源码
import re
import json
import time

class ScrapeCallback:
	def __init__(self,client=None,expires=timedelta(days=30)):
		self.db = pymongo.MongoClient("localhost",27017).cache
		self.db.job_info.create_index('timestamp',expireAfterSeconds=expires.total_seconds())

	def __call__(self,html):
		#print('html=',html)
		job_data = json.loads(html)
		items=[]
		try:
			results = job_data['content']['positionResult']['result']
		except Exception as e:
			print('job_data=',job_data)
		for result in results:
			item = {}
			time.sleep(2)
			item['_id'] = result['positionId']
			item['positionName'] = result['positionName']
			item['businessZone'] = result['businessZones']
			item['city'] = result['city']
			item['companyLabelList'] = result['companyLabelList']
			item['companySize'] = result['companySize']
			item['district'] = result['district']
			item['education'] = result['education']
			item['explain'] = result['explain']
			item['financeStage'] = result['financeStage']
			item['firstType'] = result['firstType']
			item['formatCreateTime'] = result['formatCreateTime']
			item['gradeDescription'] = result['gradeDescription']
			item['imState'] = result['imState']
			item['industryField'] = result['industryField']
			item['jobNature'] = result['jobNature']
			item['positionAdvantage'] = result['positionAdvantage']
			item['salary'] = result['salary']
			item['secondType'] = result['secondType']
			item['workYear'] = result['workYear']
			try:
				self.db.job_info.insert(item)
			except errors.DuplicateKeyError as e:
				pass
		
			



		
		

