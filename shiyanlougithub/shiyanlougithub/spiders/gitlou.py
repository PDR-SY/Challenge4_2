# -*- coding: utf-8 -*-
import scrapy
from shiyanlougithub.items import ShiyanlougithubItem

class GitlouSpider(scrapy.Spider):
	name = 'gitlou'
	allowed_domains = ['github.com']
	start_urls = ['https://github.com/shiyanlou?page={}&tab=repositories'.format(i) for i in range(1,5)]
	
	def parse(self, response):
		print(response)
		for gitlou in response.css('div#user-repositories-list ul li'):
			yield ShiyanlougithubItem({
				'name':gitlou.css('a::text').extract_first(),
				'update_time':gitlou.css('relative-time::attr(datetime)').extract_first()
				})
