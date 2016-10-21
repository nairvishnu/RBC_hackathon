from . import app
from flask import render_template, request
#from . import query_parser
from . import query_info

@app.route('/')
def index():
    search_string = request.args.get('search')
    if search_string is None:
        return render_template('index.html', title="Abacus", msg=None)
    else:
        res = query_info.what_info(search_string)
        return render_template('index.html', title="Abacus: " + search_string, msg=res)


@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

@app.route('/test', methods=['GET'])
def test():
    print("YES")
    res = query_info.what_info(request.args.get('search'))
    #d={}
    #d['ycp'] = res[0].split(': ')[1]
    #d['price'] = res[1].split(': ')[1]
    return render_template('index.html', msg=res)
