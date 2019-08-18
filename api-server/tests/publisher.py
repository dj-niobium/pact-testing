import requests
import os.path
import logging


class Publisher(object):

    def __init__(self, broker_url, consumer, provider, consumer_version, consumer_tag=None, pact_local_dir='/'):
        logging.basicConfig(level=logging.DEBUG, filename='pact_broker.log')
        self.broker_url = broker_url
        self.local_dir = pact_local_dir
        self.consumer_version = consumer_version
        self.consumer_tag = consumer_tag
        self.consumer = consumer
        self.provider = provider
        self.pact_local_path = '{}{}-{}.json'.format(self.local_dir, self.consumer.lower(), self.provider.lower())
        if os.path.exists(self.pact_local_path) is not True:
            raise Exception('The file {} was not found.'.format(self.pact_local_path))

    def publish_pact(self):
        requests.put(
            url='{}/pacts/provider/{}/consumer/{}/version/{}'.format(self.broker_url, self.provider, self.consumer,
                                                                     self.consumer_version),
            data=open(self.pact_local_path), headers={'Content-Type': 'application/json'})
        if self.consumer_tag is not None:
            Tagger(self.broker_url, self.consumer, self.consumer_version, self.consumer_tag).perform_tagging()


class Tagger(object):

    def __init__(self, broker_url, participant, version, tag):
        self.participant = participant
        self.version = version
        self.tag = tag
        self.broker_url = broker_url

    def perform_tagging(self):
        return requests.put(
            url='{}/pacticipants/{}/versions/{}/tags/{}'.format(self.broker_url, self.participant, self.version,
                                                                self.tag),
            headers={'Content-Type': 'application/json'}).raise_for_status()
