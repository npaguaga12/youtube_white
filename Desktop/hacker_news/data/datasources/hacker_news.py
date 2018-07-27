"""HackerNews Datasource

api is documented here: https://github.com/HackerNews/API"""

import requests

response = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json')
response.status_code
data = response.json()
data = data[0:10]
data """check if 10 topstory ids are stored there"""

url_template = 'https://hacker-news.firebaseio.com/v0/item/{}.json?print=pretty'
[item for item in data]
[url_template.format(item) for item in data]
urls = _ """save result url from topstories in variable"""

results = []
for url in urls:
    response = requests.get(url)
    results.append(response.json())
    print(results)

titles = [t['title'] for t in results if 'title' in t]
print(titles)

authors = [a['by'] for a in results if 'by' in a]
print(authors)

"""loop sequences using zip() function"""
for t, a, u in zip(titles, authors, urls):
    print('{0}: {1}, {2}'.format(t, a, u))



class HackerNewsDatasource(object):
    """Handles all communication with HackerNews"""
