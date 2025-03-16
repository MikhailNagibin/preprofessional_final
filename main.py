import requests
from flask import *
from our_requests import *

app = Flask(__name__)


@app.route('/')
def index():



if __name__ == "__main__":
    conn = get_db_connection()
    cur = conn.cursor()
    app.run(host='0.0.0.0', port=8000, debug=True)