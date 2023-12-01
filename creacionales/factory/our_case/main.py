from creacionales.factory.our_case.base import Scraper
from creacionales.factory.our_case.scrappers.selenium_scrapper import SeleniumScraper
from creacionales.factory.our_case.scrappers.playwright_scrapper import PlaywrightScraper


class ScraperFactory:
    _scrapers = {
        "selenium": SeleniumScraper,
        "playwright": PlaywrightScraper
        # añadir más scrapers aquí
    }

    @staticmethod
    def get_scraper(scraper_type: str) -> Scraper:
        try:
            return ScraperFactory._scrapers[scraper_type]()
        except KeyError:
            raise ValueError(f"Unknown scraper type: {scraper_type}")

def scrape_website(scraper_type: str, url: str):
    try:
        scraper = ScraperFactory.get_scraper(scraper_type)
    except ValueError as e:
        print(e)
        return

    try:
        html = scraper.fetch_data(url)
        data = scraper.parse_data(html)
        scraper.store_data(data)
    except Exception as e:
        print(f"Error during scraping: {e}")

# Ejemplo de uso
# Ejemplo de uso
# scrape_website("selenium", "https://scrapelead.io/web-scraping/")
scrape_website("playwright", "https://scrapelead.io/web-scraping/")
