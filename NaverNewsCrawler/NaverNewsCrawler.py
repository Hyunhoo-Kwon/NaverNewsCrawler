import crawler

import threading
import time
import json
import urllib.request

class NaverNewsCrawler(threading.Thread):
	jandi_url = "https://wh.jandi.com/connect-api/webhook/12439562/27b5b7ee3e66d05c52662002c36452d2"
	jandi_headers = {"Accept": "application/vnd.tosslab.jandi-v2+json", "Content-Type": "application/json"}

	def __init__(self):
		threading.Thread.__init__(self)

		params = {"body" : "Naver News Webhook Start"}
		req = urllib.request.Request(self.jandi_url, json.dumps(params).encode('utf8'), self.jandi_headers)
		response = urllib.request.urlopen(req)

	def run(self):
		previousNews = {}

		while True:
			presentNews = {}
			presentNews = crawler.crawling()
			description = ""

			for title in presentNews:
				if title in previousNews:
					pass
				else:
					description = description + title + " [" + presentNews.get(title) + "](" + presentNews.get(title) + ")\n"

			params = {"body": "NaverNews changed!", "connectColor": "#FAC11B", "connectInfo": [{"title" : "naver_news", "description" : description}]}
			req = urllib.request.Request(self.jandi_url, json.dumps(params).encode('utf8'), self.jandi_headers)
			response = urllib.request.urlopen(req)
			
			previousNews.clear()
			previousNews.update(presentNews)

			time.sleep(3600)

if __name__ == "__main__":
	service = NaverNewsCrawler()
	service.start()
