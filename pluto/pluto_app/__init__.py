from flask import Flask

app = Flask('pluto_app')

from . import views
