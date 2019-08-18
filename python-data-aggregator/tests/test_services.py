from tests.mock_server import MockApiServer
from services.inventory import Inventory
from services.shipping import Shipping
from services.account import Account

inventory_pact_server = MockApiServer("Inventory").safe_start()
shopping_pact_server = MockApiServer("Shipping").safe_start()
account_pact_server = MockApiServer("Account").safe_start()
account_api = Account("http://localhost:{}".format(account_pact_server.port))
shipping_api = Shipping("http://localhost:{}".format(shopping_pact_server.port))
inventory_api = Inventory("http://localhost:{}".format(inventory_pact_server.port))


def test_inventory_main():
    response = inventory_api.get_data()
    assert response == [{'id': 1, 'name': 'Pants', 'quantity': 15}]


def test_inventory_get_product_name():
    response = inventory_api.get_product_name(1)
    assert response == "Pants"


def test_inventory_get_quantity():
    response = inventory_api.get_quantity(1)
    assert response == 15


def test_shipping_main():
    response = shipping_api.get_data()
    assert response == [{'id': 1, 'status': 'awaiting_shipping', 'quantity': 5}]


def test_shipping_quantity_on_hold():
    response = shipping_api.get_quantity_on_hold(1)
    assert response == 5


def test_account_main():
    response = account_api.get_data()
    assert response == [
        {'id': 1, 'first_name': 'Michael', 'last_name': 'Johnson', 'address': 'London'}]


def test_get_account():
    response = account_api.get_account(1)
    assert response == {'id': 1, 'first_name': 'Michael', 'last_name': 'Johnson', 'address': 'London'}

