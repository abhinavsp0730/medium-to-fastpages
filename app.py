import os
from util import *
from export_util import save_md
medium_link = 'https://medium.com/@ankushchoubey/lessons-learned-from-my-first-deep-learning-contest-101df133cf90'


username = 'ankushchoubey'
path = '/Users/ankushchoubey/Desktop/'+username
if not os.path.isdir(path): os.mkdir(path)

def process_article(article):
    link, date, categories = article
    name = date + '-' + '-'.join(link.split('/')[-1].split('?source')[0].split('-')[:-1])

    try:
        markdown = get_medium_markdown(link)
        markdown = format_medium_markdown(markdown)
        #markdown = download_images(markdown)
        save_md(markdown,path,name)
        print('Downloaded', name)
    except:
        print('Could not download', name)

for article in get_articles(username):
    process_article(article)