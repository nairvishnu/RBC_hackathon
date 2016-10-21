from . import app
from flask import render_template, request
#from . import query_parser
from . import query_info

@app.route('/')
def index():
    all_args = request.args.to_dict()
    try:
        search_string = all_args['search']
        print(search_string)
        return render_template('index.html', title="Home", search_param=search_string)
    except KeyError:
        return render_template('index.html', title="Home")


@app.route('/test', methods=['GET'])
def test():
    print("YES")
    res = query_info.what_info(request.args.get('search'))
    #d={}
    #d['ycp'] = res[0].split(': ')[1]
    #d['price'] = res[1].split(': ')[1]
    return render_template('index.html', msg=res)
