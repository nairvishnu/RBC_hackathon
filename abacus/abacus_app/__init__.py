from flask import Flask

app = Flask('abacus_app')

from . import views
