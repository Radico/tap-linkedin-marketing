import singer

from tap_kit import TapExecutor
from tap_kit.utils import (transform_write_and_count)

LOGGER = singer.get_logger()


class LinkedInExecutor(TapExecutor):

    def __init__(self, streams, args, client):
        """
        Args:
            streams (arr[Stream])
            args (dict)
            client (BaseClient)
        """
        super(LinkedInExecutor, self).__init__(streams, args, client)

        self.url = 'https://api.linkedin.com/v2/adAnalyticsV2'
        self.authorization = self.client.config['access_token']

    def call_full_stream(self, stream):
        """
        Method to call all fully synced streams
        """
        pivots = (
            "CAMPAIGN",
            "CREATIVE",
            "CAMPAIGN_GROUP",
            "CONVERSION",
        )
        for pivot in pivots:
            request_config = {
                'url': self.url,
                'headers': self.build_headers(),
                'params': self.build_params(pivot),
                'run': True
            }

            LOGGER.info("Extracting {s} ".format(s=stream))

            self.call_stream(stream, request_config)

    def call_stream(self, stream, request_config):
        res = self.client.make_request(request_config)

        records = res.json()

        if not records:
            records = []
        elif not isinstance(records, list):
            # subsequent methods are expecting a list
            records = [records]

        transform_write_and_count(stream, records)

    def build_params(self, pivot):
        return {
            "q": "analytics",
            "pivot": pivot,
            "dateRange.start.day": 12,
            "dateRange.start.month": 1,
            "dateRange.start.year": 2019,
            "timeGranularity": "DAILY",
            "accounts[0]": "urn:li:sponsoredAccount:507638420"
        }

    def build_headers(self):
        """
        Included in all API calls
        """
        return {
                "Authorization": self.authorization,
                "Accept": "application/json;charset=UTF-8"
        }
