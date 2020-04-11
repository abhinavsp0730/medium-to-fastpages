import requests_html
import os

def get_medium_markdown(article_url):
    server = 'https://medium-to-markdown.now.sh/?url='
    url = server + article_url
    session = requests_html.HTMLSession()
    resp = session.get(url)
    resp.html.render(sleep=6)
    return resp.html.find('textarea')[0].full_text

def format_medium_markdown(markdown):
    title = get_title_from_markdown(markdown)
    markdown = '\n'.join(markdown.splitlines()[8:])
    return get_header(title,'',[]) + markdown

def get_header(title, description,categories=[],toc='true'):
    title = title.replace(':', ' ')
    return f"""---
toc: {toc}
layout: post
description: {description}
categories: [Medium]
title: {title}
---
"""

month_num_dict = {
    'Jan':'01',
    'Feb':'02',
    'Mar':'03',
    'Apr':'04',
    'May':'05',
    'Jun':'06',
    'Jul':'07',
    'Aug':'08',
    'Sep':'09',
    'Oct':'10',
    'Nov':'11',
    'Dec':'12',
}

def get_date_formatted(date):
    split = date[date.index(',')+2:].split(' ')[:3][::-1]
    split[1] = month_num_dict[split[1]]
    return '-'.join(split)

def get_title_from_markdown(markdown):
    for i in markdown.splitlines():
        if i.startswith('title: '): return i.replace('title: ', '')

def get_articles(profile):
    session = requests_html.HTMLSession()
    medium_link = f'https://medium.com/feed/@{profile}'.replace('@@','@')
    r = session.get(medium_link)
    for i in r.html.find('channel')[0].find('item'):
        link = i.find('link')[0].html.replace('<link/>', '')
        pub_date = i.find('pubDate')[0].text
        categories = i.find('category')
        yield link, get_date_formatted(pub_date), categories


def is_image(line):
    return line.startswith('![') and line.endswith(']') and 'medium.com' in line

def get_image_url(line):
    return line.replace(']', '').split('[')[-1]

def download_image(path, name, url):
    #not compelte
    if not os.path.isdir(path): os.mkdir(path)

def download_images(name, markdown):
    #not compelete
    new_markdown = []
    count = 1
    for line in markdown.splitlines():
        if is_image(line):
            download_image(name, str(count), get_image_url(line))
        else:
            new_markdown.append(line)
    return new_markdown