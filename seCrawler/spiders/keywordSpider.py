__author__ = 'tixie'
from scrapy.spiders import Spider
from searResultPages import searResultPages
from searchEngines import SearchEngineResultSelectors
from scrapy.selector import  Selector
import html2text
import requests
import nltk
from htmlst
from nltk.tokenize import sent_tokenize, word_tokenize
from htmlst import HTMLSentenceTokenizer

class keywordSpider(Spider):
    name = 'keywordSpider'
    allowed_domains = ['bing.com','google.com','baidu.com']
    start_urls = []
    keyword = None
    searchEngine = None
    selector = None


    def __init__(self, keyword, se = 'bing', pages = 50,  *args, **kwargs):
        super(keywordSpider, self).__init__(*args, **kwargs)
        self.keyword = keyword.lower()
        self.searchEngine = se.lower()
        self.selector = SearchEngineResultSelectors[self.searchEngine]
        pageUrls = searResultPages(keyword, se, int(pages))
        for url in pageUrls:
            print(url)
            try:
                example_html_one = open(url, 'r').read()
                parsed_sentences = HTMLSentenceTokenizer().feed(example_html_one)
                print(parsed_sentences)
            finally:
                print("Don!!!!!!!!!")

            self.start_urls.append(url)

    def parse(self, response):
        for url in Selector(response).xpath(self.selector).extract():
            yield {'url':url}

        pass
