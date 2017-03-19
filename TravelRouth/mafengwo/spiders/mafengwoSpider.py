import scrapy
from scrapy.selector import Selector
from mafengwo.items import MafengwoItem


class travelPathSpider(scrapy.Spider):
    name = "travelPath"
    allowed_domains = ["mafengwo.cn"]

    urls = []
    for i in range(1,800000):
        url = "http://www.mafengwo.cn/schedule/"+str(i)+".html"
        urls.append(url)

    start_urls = urls

    def parse(self, response):
        # filename = response.url.split("/")[-1] + '.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        for sel in response.xpath('/html'):
            item = MafengwoItem()
            item['title'] = sel.xpath('//h1/text()').extract()
            item['desti'] = sel.xpath('//*[@id="day1"]/div[1]/div/h2/a/text()').extract()
            item['days'] = sel.xpath('//div[@class="des_detail"]/div/span[2]/text()').extract() 
            item['payment'] = sel.xpath('//div[@class="des_detail"]/div/span[3]/text()').extract() 
            item['desc'] = sel.xpath('//div[@class="des_list _j_list"]/ul/li/text()|//div[@class="des_list _j_list"]/ul/li/strong/text()').extract()  
            yield item
