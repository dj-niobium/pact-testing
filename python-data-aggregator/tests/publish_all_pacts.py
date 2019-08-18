from tests.mock_servers_configurations import SERVICES, BASE_CONFIG
from tests.publisher import Publisher

for service in SERVICES.keys():
    broker = Publisher(broker_url="http://localhost:9292", pact_local_dir=BASE_CONFIG['path_to_pacts'],
                       consumer=BASE_CONFIG['consumer'],
                       provider=service,
                       consumer_version=111,
                       consumer_tag="prod")
    broker.publish_pact()
