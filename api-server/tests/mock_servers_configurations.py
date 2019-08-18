from pact import EachLike, Like

BASE_CONFIG = {
    'host': '127.0.0.1',
    # path to the dir where the pact files will be stored. Eventually should be centralised int the Pact Broker
    'path_to_pacts': 'pacts/python/',
    'consumer': 'api-server'
}

# each service should contain name and the following keys (case sensitive):
# 'GIVEN' - a description string about the initial data needed for using of tht API,
# 'UPON_RECEIVING' - a string description of the expected outcomes,
# 'REQUEST' - the expected request to the API (see pact.io for details),
# 'RESPONSE' the expected response from the API (see pact.io for the details)
SERVICES = {
    'python-data-aggregator': {
        'port': 1111,
        'interactions':
            [
                {
                    'GIVEN': 'Provided we have the correct project_id and data to edit',
                    'UPON_RECEIVING': 'the correct paper URL should be provided',
                    'REQUEST': {
                        'method': 'get',
                        'path': '/buy/1/1/15'
                    },
                    'RESPONSE': {
                        'status': 200, 'body': {
                            "status": Like("Transaction successful"),
                            "transaction": Like({
                                "account_name": Like("John Smith"),
                                "product_name": Like("Socks"),
                                "quantity": Like(5)
                            })
                        }
                    }

                }
            ]
    }
}
