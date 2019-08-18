from pact import Consumer, Provider
import atexit
from tests.mock_servers_configurations import BASE_CONFIG, SERVICES


class MockApiServer:
    def __init__(self, service, log_dir='contract_logs/consumer'):
        config = SERVICES[service]
        self.pact = Consumer(BASE_CONFIG['consumer']).has_pact_with(Provider(service), host_name=BASE_CONFIG['host'],
                                                                    port=config['port'],
                                                                    pact_dir=BASE_CONFIG['path_to_pacts'],
                                                                    log_dir=log_dir)
        for interaction in config['interactions']:
            (self.pact.given(interaction['GIVEN'])
             .upon_receiving(interaction['UPON_RECEIVING'])
             .with_request(**interaction['REQUEST'])
             .will_respond_with(**interaction['RESPONSE']))

    def stop(self):
        self.pact.stop_service()
        return self

    def start(self):
        self.pact.start_service()
        self.pact.setup()
        return self

    def safe_start(self):
        self.start()
        atexit.register(self.stop)
        return self.pact
