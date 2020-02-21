from tap_kit import main_method
from tap_kit import BaseClient

from .marketing import MarketingStream
from .executor import LinkedInExecutor


REQUIRED_CONFIG_KEYS = [
    "access_token",
]

STREAMS = [
    MarketingStream,
]


def main():
    main_method(
        REQUIRED_CONFIG_KEYS,
        LinkedInExecutor,
        BaseClient,
        STREAMS
    )


if __name__ == '__main__':
    main()
