from typing import Protocol


class Scraper(Protocol):

    def fetch_data(self, url: str) -> str:
        ...

    def parse_data(self, html: str):
        ...

    def store_data(self, data):
        ...

