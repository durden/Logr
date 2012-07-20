# GLOBAL CONFIGURATION

WEBSITE_NAME = 'Logr'
DEBUG = True

# ARTICLE AND PAGE CONFIGURATION

ARTICLE_DIR = 'articles/'
PAGES_DIR = 'pages/'

# NAVBAR CONFIGURATION
# Add navbar links with dict(title="Title", url="URL)

NAV = [dict(title='Home', url='/')]
       
# SECURITY CONFIGURATION

SECRET_KEY = 'SECRET_KEY'

# Accept all standard markdown file extensions.

EXTENSIONS = ('.markdown','.mdown','.mkdn','.md','.mkd','.mdwn','.mdtxt','.mdtext','.text')