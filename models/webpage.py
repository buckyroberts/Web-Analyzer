

class Webpage:

    def __init__(self, data):
        self.data = data
        self.url = self.data['url']
        self.status = self.data['status']
        self.response_headers = self.data['headers']

        self.title = self.get_tag_content('title')[0]
        self.meta_description = self.get_meta_description()

        self.links = self.get_links()
        self.images = self.get_images()

    # Returns all images as lists [src, alt]
    def get_images(self):
        results = []
        for item in self.data['tags']:
            try:
                if item['name'] == 'img':
                    src = item['attributes']['src']
                    alt = item['attributes']['alt']
                    if not src:
                        src = ''
                    if not alt:
                        alt = ''
                    results.append([src, alt])
            except KeyError:
                pass
        return results

    # Returns all links as lists [href, contents]
    def get_links(self):
        results = []
        for item in self.data['tags']:
            try:
                if item['name'] == 'a':
                    url = item['attributes']['href']
                    content = item['content']
                    if not url:
                        url = ''
                    if not content:
                        content = ''
                    results.append([url, content])
            except TypeError:
                pass
            except KeyError:
                pass
        return sorted(results)

    def get_meta_description(self):
        for item in self.data['tags']:
            if item['name'] == 'meta':
                try:
                    if item['attributes']['name'] == 'description':
                        return item['attributes']['content']
                except KeyError:
                    continue
        return None

    def get_tag_content(self, tag):
        results = []
        for item in self.data['tags']:
            if item['name'] == tag and item['content']:
                results.append(item['content'])
        return results

    def get_tag_attributes(self, tag, attr):
        results = []
        for item in self.data['tags']:
            if item['name'] == tag and item['attributes'][attr]:
                results.append(item['attributes'][attr])
        return results
