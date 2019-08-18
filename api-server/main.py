from flask import Flask, jsonify
from services.data_aggregator import DataAggregator

app = Flask(__name__)
da_api = DataAggregator("http://data-aggregator")


@app.route('/buy/<account>/<prod_id>/<quantity>')
def hello_world(account, prod_id, quantity):
    return jsonify(da_api.buy(account, prod_id, quantity))


if __name__ == '__main__':
    app.run()
