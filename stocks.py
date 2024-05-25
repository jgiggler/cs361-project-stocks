from flask import Flask, jsonify, request
import requests

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

API_KEY = 'bhq95ptRLIpFKjfocIo0nwN8clvWPjU_'

@app.route('/stock/<symbol>', methods=['GET', 'POST'])
def get_stock_price(symbol):
    data = request.json
    symbol = data.get('symbol')
    symbol = symbol.upper()
    date_start = data.get('time_start')
    date_end = data.get('time_end')
    
    STOCK_API_URL = f"https://api.polygon.io/v2/aggs/ticker/{symbol}/range/1/day/{date_start}/{date_end}?apiKey={API_KEY}"
    
    # Call API with user submitted data
    response = requests.get(f"{STOCK_API_URL}")
    data = response.json()
    print(data)
    return jsonify(data)

if __name__ == '__main__':
    app.run(port=5151)
    
