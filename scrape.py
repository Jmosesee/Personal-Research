import requests
from bs4 import BeautifulSoup
from database import get_keywords, get_interests
import urllib.parse

# Determines whether the anchor tag is a link to a wikipedia article or not
def test_anchor(tag, url):
    if (tag.get('href') is not None and
        tag['href'].startswith(r'/wiki/') and
        tag['href'][:8] != "#CITEREF" and 
        not tag['href'].startswith(url[len("https://en.wikipedia.org/wiki/"):] + '#', 6) and
        '/' not in tag['href'][6:]):
            return True
    else:
        return False

# def scrape(url):
#     keywords = [k[0] for k in get_keywords()]
#     # print(keywords)
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     a_tags = []
#     p_tags = soup.find(id="bodyContent").find_all('p')
#     for p_tag in p_tags:
#         a_tags.extend([tag for tag in p_tag.find_all('a') 
#             if tag.parent.name == "p" and 
#                 tag.get('href') is not None and
#                 tag['href'].startswith(r'/wiki/') and
#                 tag['href'][:8] != "#CITEREF" and 
#                 urllib.parse.unquote(tag['href'][6:].split('#')[0]) not in keywords and
#                 not tag['href'].startswith(url[len("https://en.wikipedia.org/wiki/"):] + '#', 6)])    
#     # print(url[len("https://en.wikipedia.org/wiki/"):])
#     # print(a_tags[0]['href'][6:])
#     # print(urllib.parse.unquote(a_tags[0]['href'][6:]))
#     return  a_tags

def scrape2(url):
    global a_id
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    keywords = dict(get_keywords())
    classes = {1: 'Interested',
                0: 'Not_Interested',
                -1: 'Undecided',
                2: 'Satisfied'}

    def highlight(p):
        global a_id
        for a in p('a'):
            if test_anchor(a, url):
                keyword = urllib.parse.unquote(a['href'][6:].split('#')[0])
                if keyword in keywords:   # Todo: Can we use get instead of this condition?
                    a['class'] = a.get('class', []) + [classes[keywords[keyword]]]
                a['onclick'] = f"hello({a_id}); return true;"
                a['id'] = a_id
                a_id += 1
        return p

    a_id = 1
    scraped = {
        'title': soup.find('h1').text,
        'p': list(map(highlight, soup('p'))),
        'url': url
    }

    return scraped

# def disinterest_preceding(scraped, path):
#     keywords = dict(get_keywords())
#     for p in scraped['p']:
#         for a in p('a'):
#             if test_anchor(a, scraped['url']):
#                 keyword = a['href'][6:].split('#')[0]
#                 if keyword == path:
#                     return
#                 else:
#                     print('Testing 2')
#                     if not (keyword in keywords and keywords[keyword] >= 1):
#                         log_interested(keyword, -1)
