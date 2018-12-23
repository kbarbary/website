# -*- coding: utf-8 -*-

import time


# Data about this site
BLOG_AUTHOR = "Kyle Barbary"
BLOG_TITLE = "Kyle Barbary"
SITE_URL = "http://www.kylebarbary.com/"
BLOG_EMAIL = "kylebarbary@gmail.com"
BLOG_DESCRIPTION = ""

# What is the default language?
DEFAULT_LANG = "en"

# What other languages do you have?
# The format is {"translationcode" : "path/to/translation" }
# the path will be used as a prefix for the generated pages location
TRANSLATIONS = {
    DEFAULT_LANG: "",
    # Example for another language:
    # "es": "./es",
}


TRANSLATIONS_PATTERN = '{path}.{lang}.{ext}'


# Links for the sidebar / navigation bar.
# You should provide a key-value pair for each used language.
NAVIGATION_LINKS = {
    DEFAULT_LANG: (
        ('/software', 'code'),
        ('/blog', 'blog'),
#        ('/categories/index.html', 'Tags'),
#        ('/rss.xml', 'RSS'),
    ),
}

NAVIGATION_ALT_LINKS = {
    DEFAULT_LANG: {}
}

import os
EXTRA_THEMES_DIRS = [
    os.path.join(os.path.dirname(__file__), "themes")
    ]
THEME = 'iceland'
THEME_COLOR = '#5670d4'

POSTS = (
    ("posts/*.rst", "blog", "post.tmpl"),
)
PAGES = (
    ("pages/*.rst", "", "story.tmpl"),
    ("pages/*.html", "", "story.tmpl"),
)

COMPILERS = {
    "rest": ('.rst', '.txt'),
    "markdown": ('.md', '.mdown', '.markdown'),
    "textile": ('.textile',),
    "txt2tags": ('.t2t',),
    "bbcode": ('.bb',),
    "wiki": ('.wiki',),
    #"ipynb": ('.ipynb',),
    "html": ('.html', '.htm'),
    # Pandoc detects the input from the source filename
    # but is disabled by default as it would conflict
    # with many of the others.
    # "pandoc": ('.rst', '.md', '.txt'),
}

HIDDEN_TAGS = ['mathjax']


WRITE_TAG_CLOUD = False


INDEX_PATH = "blog"


CREATE_SINGLE_ARCHIVE = True
ARCHIVE_PATH = "archive"


DATE_FORMAT = 'YYYY-MM-dd'


INDEX_TEASERS = True

LICENSE = ""


CONTENT_FOOTER = """<hr>
&copy; {date}  {author} |
built with <a href="http://getnikola.com" rel="nofollow">nikola</a> |
<a href="http://github.com/kbarbary/website">site source</a> and
<a href="https://github.com/kbarbary/website/tree/master/themes/iceland">theme</a>"""
CONTENT_FOOTER = CONTENT_FOOTER.format(author=BLOG_AUTHOR,
                                       date=time.gmtime().tm_year)


COMMENT_SYSTEM = None #"disqus"
COMMENT_SYSTEM_ID = None #"kbarbary"


PRETTY_URLS = True


SOCIAL_BUTTON_CODE = ""


SHOW_SOURCELINK = False
COPY_SOURCES = False


BODY_END = """
<script type="text/javascript">

  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-48255812-1']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();

</script>
"""


USE_BUNDLES = False


LOGGING_HANDLERS = {
    'stderr': {'loglevel': 'WARNING', 'bubble': True},
}

GLOBAL_CONTEXT = {}
