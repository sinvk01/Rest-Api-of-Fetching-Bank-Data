import json
import os
import psycopg2
from pip._internal.cli.autocompletion import autocomplete
from psycopg2.extras import RealDictCursor
import json
from flask_cors import CORS
from flask import Flask, request, jsonify
# 
# db_host = os.environ['POSTGRESQL_ADDON_HOST']
# db_name = os.environ['POSTGRESQL_ADDON_DB']
# db_user = os.environ['POSTGRESQL_ADDON_USER']
# db_URI = os.environ['POSTGRESQL_ADDON_URI']
# db_password = os.environ['POSTGRESQL_ADDON_PASSWORD']

# try:
#     conn = psycopg2.connect(
#         f"dbname='{db_name}' user='{db_user}' host='{db_host}' password='{db_password}'")
#     print("Database connected")
# except:
#     print("Not able to connect to Database")

# 
# def autocomplete(keyword, limit, offset):
#     cursor = conn.cursor(cursor_factory=RealDictCursor)
#     sql_query = f'''select
#                    *
#                    from
#                    branches
#                    where
#                    branch like '%{keyword}%'
#                    order by ifsc
#                    limit {limit} ; '''
#     cursor.execute(sql_query)
#     record = cursor.fetchall()
# 
#     return record
# 
# 
# def getBranch(keyword, limit, offset):
#     cursor = conn.cursor(cursor_factory=RealDictCursor)
#     sql_query = f'''
#                     select
#                 *
#                 from
#                 branches
#                 where
#                 address like '%{keyword}%'
#                 or branch like '%{keyword}%'
#                 or city like '%{keyword}%'
#                 or district like '%{keyword}%'
#                 or state like '%{keyword}%'
# 
#                 order by
#                 ifsc
#                 limit
#                 {limit} 
#                 offset {offset};
#             '''
#     cursor.execute(sql_query)
#     record = cursor.fetchall()
# 
#     return record


app = Flask(__name__)
CORS(app)
app.config['JSON_SORT_KEYS'] = False

branches = [
    {
        "ifsc": "ABHY0065001",
        "bank_id": 60,
        "branch": "RTGS-HO",
        "address": "ABHYUDAYA BANK BLDG., B.NO.71, NEHRU NAGAR, KURLA (E), MUMBAI-400024",
        "city": "MUMBAI",
        "district": "GREATER MUMBAI",
        "state": "MAHARASHTRA"
    }, {
        "ifsc": "ABNA0000001",
        "bank_id": 110,
        "branch": "RTGS-HO",
        "address": "414 EMPIRE COMPLEX, SENAPATI BAPAT MARG LOWER PAREL WEST MUMBAI 400013",
        "city": "MUMBAI",
        "district": "GREATER BOMBAY",
        "state": "MAHARASHTRA"
    }, {
        "ifsc": "ADCB0000001",
        "bank_id": 143,
        "branch": "RTGS-HO",
        "address": "75, REHMAT MANZIL, V. N. ROAD, CURCHGATE, MUMBAI - 400020",
        "city": "MUMBAI",
        "district": "MUMBAI CITY",
        "state": "MAHARASHTRA"
    }, {
        "ifsc": "ADCC0000001",
        "bank_id": 61,
        "branch": "RTGS-HO",
        "address": "THE AKOLA DISTRICT CENTRAL COOP. BANK LTD., P.B.NO. 8, CIVIL LINES, S.A. COLLEGE ROAD, "
                   "AKOLA. 444001",
        "city": "AKOLA",
        "district": "AKOLA",
        "state": "MAHARASHTRA"
    }, {
        "ifsc": "ABNA0100318",
        "bank_id": 110,
        "branch": "BANGALORE",
        "address": "PRESTIGE TOWERS', GROUND FLOOR, 99 & 100, RESIDENCY ROAD, BANGALORE 560 025.",
        "city": "BANGALORE",
        "district": "BANGALORE URBAN",
        "state": "KARNATAKA"
    }, {
        "ifsc": "ADCB0000002",
        "bank_id": 143,
        "branch": "BANGALORE",
        "address": "CITI CENTRE, 28, CHURCH STREET, OFF M. G. ROAD BANGALORE 560001",
        "city": "BANGALORE",
        "district": "BANGALORE URBAN",
        "state": "KARNATAKA"
    }, {
        "ifsc": "ALLA0210217",
        "bank_id": 11,
        "branch": "K. G. ROAD",
        "address": "NO. 2, FKCCI BUILDING , K G ROAD , BANGALORE",
        "city": "BANGALORE",
        "district": "BANGALORE URBAN",
        "state": "KARNATAKA"
    }, {
        "ifsc": "ALLA0210326",
        "bank_id": 11,
        "branch": "BANGALORE BASAVANGUDI",
        "address": "121, RM COMPLEX, DR.D.V.GUNDAPPA ROAD, BASAVANGUDI, BANGALORE - 560004",
        "city": "BANGALORE",
        "district": "BANGALORE URBAN",
        "state": "KARNATAKA"

    }
]


@app.errorhandler(404)
def not_found(e):
    return '''
            <h1>bad request!</h1> 
            Endpoint: /api/branches?q=<>
            Endpoint: /api/branches/autocomplete?q=<>
            ''', 400


@app.route('/')
def index():
    return 'Welcome to Banks Data'


@app.route('/branches/autocomplete')
def fetch():
    search_query = request.args['q']

    try:
        limit = request.args['limit']
    except:
        limit = 5

    try:
        offset = request.args['offset']
    except:
        offset = 0
    data = {"branches": autocomplete(search_query.upper(), limit, offset)}

    return jsonify(data)


def getBranch(param, limit, offset):
    pass


@app.route('/api/branches')
def branch():
    search_query = request.args['q']

    try:
        limit = request.args['limit']
    except:
        limit = 5

    try:
        offset = request.args['offset']
    except:
        offset = 0
    data = {"branches": getBranch(search_query.upper(), limit, offset)}

    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
