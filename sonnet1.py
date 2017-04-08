# -*- coding: utf-8 -*-
#Create a scrapy project and a spider named sonnet1. This is the code for that spider.
import scrapy
import csv
with open('Sonnets.csv', 'a', newline='') as csvfile:
        headings = ['Number', 'Sonnet']
        writer = csv.DictWriter(csvfile, fieldnames=headings)
        writer.writeheader()
class Sonnet1Spider(scrapy.Spider):
    name = "sonnet1"
    allowed_domains = ["www.opensourceshakespeare.org"]
    start_urls = ['http://www.opensourceshakespeare.org/views/sonnets/sonnets.php']

    def parse(self, response):
        links = []
        links = response.css('tr[align="left"] p.medium_mono a::attr(href)').extract()
        for link in links:
            next_page = response.urljoin(link)
            yield scrapy.Request(next_page,callback=self.sonnet_parse)
    def sonnet_parse(self,response):
        l = []
        l = response.css('p.normalsans::text').extract()
        z=[]
        for i in l:
            z.append(i.replace('\xa0','').replace('\n',''))
        flag=0
        for i in range(len(response.url)):
            if response.url[i]=='=':
                flag=1
                break
        if flag==1:
            i=i+1
            s = response.url[i::]
        prod_dict = {'Number': s, 'Sonnet': ' '.join(z)}
        with open('Sonnets.csv', 'a', newline='') as csvfile:
                headings = ['Number', 'Sonnet']
                writer = csv.DictWriter(csvfile, fieldnames=headings)
                writer.writerow(prod_dict)
