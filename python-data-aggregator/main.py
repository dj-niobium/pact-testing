from flask import Flask, jsonify
from services.inventory import Inventory
from services.shipping import Shipping
from services.account import Account
from controllers.validator import Validator

inventory_api = Inventory("http://inventory")
shipping_api = Shipping("http://shipping")
account_api = Account("http://account")

validator = Validator(inventory_api, shipping_api)

app = Flask(__name__)


@app.route('/buy/<account>/<prod_id>/<quantity>')
def hello_world(account, prod_id, quantity):
    prod_id = int(prod_id)
    account = int(account)
    quantity = int(quantity)
    a = inventory_api.get_quantity(prod_id)
    prod_name = inventory_api.get_product_name(prod_id)
    b = shipping_api.get_quantity_on_hold(prod_id)
    account_name = account_api.get_account(account)
    if validator.is_available(prod_id, quantity):
        return jsonify({
            "status": "Transaction successful",
            "transaction": {
                "account_name": "{} {}".format(account_name["first_name"], account_name["last_name"]),
                "product_name": prod_name,
                "quantity": quantity
            }
        })
    else:
        return jsonify({
            "status": "Error. There's not enough product in the warehouse"
        })


if __name__ == '__main__':
    app.run()
