from models.webpage import Webpage
from tools.general import *


data = read_json('sample_data/1.json')
webpage = Webpage(data)

print(webpage.url)
print(webpage.status)

print(webpage.title)
print(webpage.meta_description)
print(webpage.links)
print(webpage.images)
