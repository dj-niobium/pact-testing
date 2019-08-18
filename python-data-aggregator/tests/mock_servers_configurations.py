from pact import EachLike, Like

BASE_CONFIG = {
    'host': '127.0.0.1',
    # path to the dir where the pact files will be stored. Eventually should be centralised int the Pact Broker
    'path_to_pacts': 'pacts/python/',
    'consumer': 'python-data-aggregator'
}

# each service should contain name and the following keys (case sensitive):
# 'GIVEN' - a description string about the initial data needed for using of tht API,
# 'UPON_RECEIVING' - a string description of the expected outcomes,
# 'REQUEST' - the expected request to the API (see pact.io for details),
# 'RESPONSE' the expected response from the API (see pact.io for the details)
SERVICES = {
    'Inventory': {
        'port': 1111,
        'interactions':
            [
                {
                    'GIVEN': 'Provided we have the correct project_id and data to edit',
                    'UPON_RECEIVING': 'the correct paper URL should be provided',
                    'REQUEST': {
                        'method': 'get',
                        'path': '/'
                    },
                    'RESPONSE': {
                        'status': 200, 'body': EachLike({
                            "id": Like(1),
                            "name": Like("Pants"),
                            "quantity": Like(15)
                        })
                    }

                }
            ]
    },
    'Shipping': {
        'port': 2222,
        'interactions':
            [
                {
                    'GIVEN': 'Provided we have the correct project_id and data to edit',
                    'UPON_RECEIVING': 'the correct paper URL should be provided',
                    'REQUEST': {
                        'method': 'get',
                        'path': '/'
                    },
                    'RESPONSE': {
                        'status': 200, 'body': EachLike({
                            "id": Like(1),
                            "status": Like("awaiting_shipping"),
                            "quantity": Like(5)
                        })
                    }

                }
            ]
    },
    'Account': {
        'port': 3333,
        'interactions':
            [
                {
                    'GIVEN': 'Provided we have the correct project_id and data to edit',
                    'UPON_RECEIVING': 'the correct paper URL should be provided',
                    'REQUEST': {
                        'method': 'get',
                        'path': '/'
                    },
                    'RESPONSE': {
                        'status': 200, 'body': EachLike({
                            "id": Like(1),
                            "first_name": Like("Michael"),
                            "last_name": Like("Johnson"),
                            "address": Like("London")
                        })
                    }

                }
            ]
    }
}
