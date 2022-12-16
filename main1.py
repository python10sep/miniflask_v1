"""
NOTES

1. Our first basic application runs on `localhost` (IP address - 127.0.0.1)
2. You
"""

from flask import Flask

# Flask` is the class we use to instantiate an application.
app = Flask(__name__)


# `route` decorator allows us to bind function to certain `relative URL path`.
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
