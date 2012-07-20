import os
from os import listdir

from flask import Flask, render_template
from flaskext.markdown import Markdown

from utils import list_articles, slugify

logr = Flask(__name__)
logr.config.from_object('config')
logr.config['ARTICLES'] = list_articles()
Markdown(logr)

ARTICLE_DIR = logr.config['ARTICLE_DIR']
PAGES_DIR = logr.config['PAGES_DIR']
ARTICLES = logr.config['ARTICLES']
EXTENSIONS = logr.config['EXTENSIONS']

@logr.route('/')
def index():
    """
    Render a template to hold the front page blurb.
    """
    with open(os.path.join(PAGES_DIR, 'FrontPage.md'), 'r') as f:
        blurb = f.read().decode('utf8')

    return render_template('index.html', articles=ARTICLES, blurb=blurb)

@logr.route('/b/<slug>', methods=['GET'])
def show(slug):
    """
    Search the `articles` directory for an article whose slug matches the URL
    parameter. When we find the article, render it.
    """
    # Find the right article
    for file_ in listdir(ARTICLE_DIR):
        if file_.endswith(EXTENSIONS)
            with open(os.path.join(ARTICLE_DIR, file_), 'r') as f:
                if slug == slugify(f.readline()):
                    article = os.path.join(ARTICLE_DIR, file_)
                    break

    # Now that we've found the right article, let's process it.
    with open(article, 'r') as f:
        lines = f.read().split('\n')
        
        # We don't need title or category, but it's easier to explicitly state
        # why we're popping the first two lines.
        title = lines.pop(0).strip() # Title should appear on the first line
        category = lines.pop(0).strip() # Category should appear on the second

        source = '\n'.join(lines).decode('utf8')
        
    return render_template('show.html', article=dict(source=source))
    
if __name__ == '__main__':
    logr.run()
