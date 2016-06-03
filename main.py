from models.webpage import Webpage
from models.analytics import Analytics
from tools.general import *


data = read_json('sample_data/1.json')
webpage = Webpage(data)
analytics = Analytics(data)

print('\n' + 'URL:')
print(webpage.url)

print('\n' + 'Status:')
print(webpage.status)

print('\n' + 'Content length:')
print(len(analytics.content))

print('\n' + 'Title:')
print(webpage.title)

print('\n' + 'Meta description:')
print(webpage.meta_description)

print('\n' + 'Links:')
for link in webpage.links:
    print(link)

print('\n' + 'Images:')
for image in webpage.images:
    print(image)

print('\n' + 'Headings:')
heading_tags = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']
for h in heading_tags:
    for x in webpage.get_tag_content(h):
        print(h + ' - ' + x)

print('\n' + 'Paragraphs:')
for i, x in enumerate(webpage.get_tag_content('p')):
    print(str(i+1) + ' - ' + x)

print('\n' + 'Keyword frequency:')
for item in analytics.keyword_count:
    print(str(item[1]) + ' - ' + item[0])
