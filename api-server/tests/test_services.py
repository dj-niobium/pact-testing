from tests.mock_server import MockApiServer
from services.data_aggregator import DataAggregator

da_pact_server = MockApiServer("python-data-aggregator").safe_start()
da_api = DataAggregator("http://localhost:{}".format(da_pact_server.port))


def test_data_aggregator():
    response = da_api.buy(1, 1, 15)
    assert response == {'status': 'Transaction successful',
                        'transaction': {'account_name': 'John Smith', 'product_name': 'Socks', 'quantity': 5}}
