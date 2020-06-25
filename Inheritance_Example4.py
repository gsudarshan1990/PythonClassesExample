class Ad:
    def __init__(self,owner,link,click,views):
        self.owner = owner
        self.link = link
        self.num_click = click
        self.num_view = views

class HouseAd(Ad):
    def __init__(self,owner,link,click,views,address,price):
        Ad.__init__(self,owner,link,click,views)
        self.address = address
        self.price = price
class ProductAd(Ad):
    def __init__(self,owner,link,click,views,product_description,product_price):
        Ad.__init__(self,owner,link,click,views)
        self.product_description = product_description
        self.product_price = product_price

ha=HouseAd("sonu","www.hyd.com",100,120,'chaitanyapuri',100000)
pa=ProductAd("sonu","www.open.com",120,232,"patan",20000)
print(ha.address)
print(pa.product_description)