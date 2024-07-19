#!/usr/bin/env python3
"""
Flask Application for Babel
"""

from flask import Flask, render_template, g, request, current_app
from flask_babel import Babel, gettext

class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

babel = Babel()
"Babel Instantiation"

def get_locale() -> str:
    user = getattr(g, 'user', None)
    if user is not None:
        return user.locale
    best_match_language = current_app.config['LANGUAGES']
    return request.accept_languages.best_match(best_match_language)


app = Flask(__name__)
app.config.from_object(Config)
babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def index() -> str:
    """
    Index Page
    """
    home_title = gettext('Welcome to my website')
    home_header = gettext('Hello, World')
    return render_template ('3-index.html', home_header=home_header, home_title=home_title)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)





