# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from datetime import datetime
from shiyanlougithub.models import GitLou,engine
from shiyanlougithub.items import ShiyanlougithubItem
from sqlalchemy.orm import sessionmaker

class ShiyanlougithubPipeline(object):
	def process_item(self, item, spider):
		item['name'] = item['name'].scrip()
		item['update_time'] = datetime.strptime(item['update_time'],'%Y-%m-%d %H:%M:%S')
		self.session.add(GitLou(**item))
		return item
	def open_spider(self,spider):
		Session = sessionmaker(bind = engine)
		self.session = Session()

	def close_spider(self,spider):
		self.session.commit()
		self.session.close()
