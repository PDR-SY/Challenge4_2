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
			item =  ShiyanlougithubItem({
				'name':gitlou.css('a::text').extract_first(),
				'update_time':gitlou.css('relative-time::attr(datetime)').extract_first()
				})
			url = response.urljoin(gitlou.css('a::attr(href)').extract_first())
			print('url',url)
			request = scrapy.Request(url,callback = self.parse_detail)
			request.meta['item'] = item
			yield request
	def parse_detail(self,response):
		item = response.meta['item']
		item['commits'] = (response.css('li.commits a span::text').extract_first()).strip()
		item['branches'] = (response.css('ul.numbers-summary li:nth-child(2) a span::text').extract_first()).strip()
		item['releases'] = (response.css('ul.numbers-summary li:nth-child(3) a span::text').extract_first()).strip()
		yield item