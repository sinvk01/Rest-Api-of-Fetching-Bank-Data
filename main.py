import psycopg2
from flask import Flask, request, jsonify
from psycopg2.extras import RealDictCursor

try:
    conn = psycopg2.connect(host="localhost",
                            dbname="postgres",
                            user="postgres",
                            password="Sinha85818",
                            port="5432")
    print("Connected")
except:
    print("Not Connected")


def autocomplete(keyword, limit, offset):
    cur = conn.cursor(cursor_factory=RealDictCursor)
    Query = f"""select * from branches where branch like '%{keyword}%' 
            order by ifsc limit {limit};"""
    cur.execute(Query)
    data = cur.fetchall()
    return data


def branch(keyword, limit, offset):
    cur = conn.cursor(cursor_factory=RealDictCursor)
    Query = f'''select * from branches where address like '%{keyword}%'
            or branch like '%{keyword}%'
            or city like '%{keyword}%'
            or district like '%{keyword}%'
            or state like '%{keyword}%'
            order by ifsc limit {limit} offset {offset};
            '''
    cur.execute(Query)
    data = cur.fetchall()
    return data


app = Flask(__name__)


@app.errorhandler(404)
def not_found(e):
    return ''' Bad Request''', 400


@app.route('/api/branches/autocomplete')
def auto_branch():
    search_query = request.args['q']

    try:
        limit = request.args['limit']
    except:
        limit = 10

    try:
        offset = request.args['offset']
    except:
        offset = 0
    data = {"branches": autocomplete(search_query.upper(), limit, offset)}

    return jsonify(data)


@app.route('/api/branches')
def bank():
    search_query = request.args['q']

    try:
        limit = request.args['limit']
    except:
        limit = 10

    try:
        offset = request.args['offset']
    except:
        offset = 0
    data = {"branches": branch(search_query.upper(), limit, offset)}

    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)

# app = Flask(__name__)
#
#
# @app.errorhandler(404)
# def error(e):
#     return ''' found error '''
#
#
# @app.route('/api/branches/autocomplete')
# def auto():
#
#
#
# @app.route('/api/branches')
# def branching():
#
#
# if __name__ == "__main__":
#     app.run(debug=True)
