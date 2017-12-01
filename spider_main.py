# -*- coding: utf-8 -*-
# @Author: liang
# @Date:   2017-11-30 19:25:52
# @Last Modified by:   liang
# @Last Modified time: 2017-11-30 20:08:16

class SpiderMain():
	def __init__(slef):
		self.urls = url_manager.UrlManager()
		self.downloader = html_downloader.HtmlDownloader()
		self.paser = html_parser.HtmlParser()
		self.outputer = html_outputer.HtmlOutputer()

	def craw(self, root_url):
		

if __name__=='__main__':
	root_url = 'https://uniqlo.tmall.com/'
	objSpider = SpiderMain()
	objSpider.craw(root_url)