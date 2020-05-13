import os
from util import *
from export_util import save_md
medium_link = 'https://medium.com/@ankushchoubey/lessons-learned-from-my-first-deep-learning-contest-101df133cf90'


username = 'ankushchoubey'
path = '/content/medium-to-fastpages' + username
if not os.path.isdir(path): os.mkdir(path)

def process_article(article):
    link, date, categories = article
    name = date + '-' + '-'.join(link.split('/')[-1].split('?source')[0].split('-')[:-1])

    try:
        markdown = get_medium_markdown(link)
        markdown = format_medium_markdown(markdown)
        markdown = download_images(path, name, markdown)
        save_md(markdown,path,name)
        print('Downloaded', name)
    except Exception as e:
        print(e)
        print('Could not download', name)

# Getting via RSS Feed
for article in get_articles(username):
    process_article(article)

# Medium RSS now only  allows 10 latest articles; I had to manually create list of my other articles to add
posts = [
    ['https://medium.com/@ankushchoubey/easy-jupyter-notebook-tips-1cc5bcf27002', '2019-07-29'],
    ['https://medium.com/@ankushchoubey/clean-code-1-flat-is-better-than-nested-leave-when-not-okay-c09ba74090ef', '2019 12 20'],
    ['https://medium.com/@ankushchoubey/clean-code-2-leave-clues-naming-convention-89932c18abac', '2019 12 20'],
    ['https://medium.com/@ankushchoubey/my-top-10-un-popular-google-collab-tips-53e7b57e3248', '2019 08 18'],
    ['https://medium.com/@ankushchoubey/series-tips-on-writing-clean-code-30d717f32ae4', '2019 12 19'],
]

for post in posts:
    post[1] = post[1].replace(' ','-')
    process_article(post+['Deep Learning'])
