# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class Acitem(Item):
    url        = Field()
    acNo       = Field()
    title      = Field()
    time       = Field()
    click       = Field()
    dm      = Field()
    coin     = Field()
    sc    = Field()
    up  = Field()
    comment = Field()
    category = Field()
	
