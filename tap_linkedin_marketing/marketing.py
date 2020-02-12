from tap_kit.streams import Stream
import singer

LOGGER = singer.get_logger()


class MarketingStream(Stream):

    stream = 'marketing'

    meta_fields = dict(
        # key_properties=['snapped_lat'],
        # api_path='/score',
        replication_method='full',
        selected_by_default=False

    )

    schema = {
        "properties": {

        }
    }

