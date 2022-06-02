#App.py
#CS 361 Final Project - Stephen Oium
#This is the final build for my application "OER Books"
# OER is open educational resources.
# this application displays oer textbooks for free so students can download them
# this app also has a website at 5tephenswebsite.000webhostapp.com/OER.html
# All rights reserved
# Stephen Oium
# Enjoy

from flask import Flask
from views import views



app = Flask(__name__)
app.register_blueprint(views, url_prefix="/")

if __name__ == '__main__':
    app.run(debug=True)
