class Spider:
    total_number=8
    def __init__(self,code,species,weight,size):
        self.code = code
        self.species = species
        self.weight = weight
        self.size = size

print(Spider.total_number)
Spider.total_number=10
print(Spider.total_number)

my_spider = Spider("xxx","spider1","100","12")
print(my_spider.total_number)