import urllib.request as ur
from bs4 import BeautifulSoup

url = "http://news.naver.com/main/history/mainnews/index.nhn"
presentNews = {}

def crawling(url = "http://news.naver.com/main/history/mainnews/index.nhn"):
	html_doc = ur.urlopen(url).read()
	webData = BeautifulSoup(html_doc, 'html.parser')
	for section in webData.find_all("div", "newsnow"):
		for news in section.find_all("a"):
			title = news.get_text().strip()
			link = news.get("href")
			presentNews[title] = link
	return presentNews
