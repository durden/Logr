import os

from flask import Flask, render_template
from flaskext.markdown import Markdown
from os import listdir
from utils import list_articles, slugify

logr = Flask(__name__)
logr.config.from_object('config')
logr.config['ARTICLES'] = list_articles()
Markdown(logr)

ARTICLE_DIR = logr.config['ARTICLE_DIR']
PAGES_DIR = logr.config['PAGES_DIR']
ARTICLES = logr.config['ARTICLES']
EXTENSIONS = logr.config['EXTENSIONS']
FRONT_PAGE = logr.config['FRONT_PAGE']

@logr.route('/')
def index():
    """
    Renders the front page.
    """
    with open(os.path.join(PAGES_DIR, FRONT_PAGE), 'r') as f:
        source = f.read().decode('utf8')
    return render_template('index.html', article=ARTICLES, source=source)

@logr.route('/b/<slug>', methods=['GET'])
def show(slug):
    """
    Search the `articles` directory for an article whose slug matches the URL
    parameter. When we find the article, render it.
    """
    article = None

    # Searching articles ..
    for file_ in listdir(ARTICLE_DIR):
        if file_.endswith(EXTENSIONS):
            with open(os.path.join(ARTICLE_DIR, file_), 'r') as f:
                if slug == slugify(f.readline()):
                    article = os.path.join(ARTICLE_DIR, file_)
                    break

    # If we didn't find the article, it doesn't exist.
    if not article:
        article = os.path.join(PAGES_DIR, 'article-404.md')

    with open(article, 'r') as f:
        lines = f.read().split('\n')
        # Title should be the first line of the file. 
        title = lines.pop(0).strip().decode('utf8')
        # Category should be second.
        category = lines.pop(0).strip().decode('utf8')
        # The rest is the article itself.
        source = '\n'.join(lines).decode('utf8')
        
    return render_template('show.html', article=dict(title=title, source=source))
    
if __name__ == '__main__':
    logr.run()
