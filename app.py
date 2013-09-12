# -*- coding: utf-8 -*-
from flask import Flask, request, redirect, render_template, url_for

from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import guess_lexer

import urllib

app = Flask(__name__)

@app.route('/')
def highlight_file():
    # 1. if url not given redirect to index.html
    if request.query_string == '':
        return redirect(url_for('static', filename='index.html'))
    # 2. retrieve url
    f = urllib.urlopen(request.query_string)
    code = f.read(1024*1024)
    # 3. syntax highlight with Pygments
    # 4. render
    code = highlight(code, guess_lexer(code), HtmlFormatter(linenos=True))
    return render_template("highlight.html", code=code)

if __name__ == '__main__':
    app.run()
