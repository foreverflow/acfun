from scrapy.spiders import Spider
import re, urllib2
from scrapy.selector import HtmlXPathSelector
from AcfunCrawler.items import Acitem 

class DmozSpider(Spider):
    name = "acfunspider"
    allowed_domains = ['acfun.tv']
    start_urls = []

    def __init__(self, begin = None, end = None):
        if begin is None:
            begin = 1
        if end is None:
            end = 100000

        for i in range(int(begin), int(end)):     
                self.start_urls.append('http://www.acfun.tv/v/ac' + str(2610666 - i))


    def parse(self, response):
        hxs = HtmlXPathSelector(response)

        Ac = Acitem()
        Ac['url']       = response.url    
        Ac['title']     = hxs.xpath("//h1/text()").extract()[0]
        Ac['time']      = hxs.xpath("/html/body/div/div[7]/div/div[1]/div[1]/div[1]/p/span[2]/text()").extract()[0]
        Ac['acNo']      = int(re.search(r'\d+', str(response.url)).group())
        Ac['up']        = hxs.xpath("/html/body/div/div[7]/div/div[1]/div[1]/div[1]/div[2]/div[1]/a[1]/text()").extract()[0]
        Ac['category']  = hxs.xpath("/html/body/div/div[7]/div/div[1]/div[1]/p/a[2]/text()").extract()[0]		
        if Ac['up']:
            content = urllib2.urlopen("http://www.acfun.tv/content_view.aspx?contentId=" + re.search(r'\d+', str(response.url)).group()).read()
            contentnumber =  re.findall(re.compile(r"\d*"),content)
            Ac['click'] = contentnumber[1]
            Ac['dm'] =contentnumber[9]
            Ac['coin'] =contentnumber[13]
            Ac['sc'] =contentnumber[11]
            Ac['comment'] =contentnumber[3]

        yield Ac
    