from . import app
from flask import render_template, request

@app.route('/')
def index():
    all_args = request.args.to_dict()
    try:
        search_string = all_args['search']
        print(search_string)
        return render_template('index.html', title="Home", search_param=search_string)
    except KeyError:
        return render_template('index.html', title="Home")


