from . import app
from flask import render_template, Flask, request
import query_info
@app.route('/')
def index():

    all_args = request.args.to_dict()
    try:
        search_string = all_args['search']
<<<<<<< HEAD
        the_info = query_info.what_info(search_string)
        the_info_list = [item for sublist in the_info for item in sublist] #list comprehension here to flatten list.
        return render_template('index.html', title="Home", search_param=search_string, mytest=the_info_list)
=======
        if search_string == "":
            return render_template('index.html', title="Home")
        else:
            return render_template('index.html', title="Home", search_param=search_string)
>>>>>>> upstream/master
    except KeyError:
        return render_template('index.html', title="Home")
