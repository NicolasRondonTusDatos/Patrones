from playwright.sync_api import sync_playwright


class PlaywrightScraper:
    def fetch_data(self, url: str) -> str:
        with sync_playwright() as p:
            # Inicializa el navegador en modo headless
            browser = p.chromium.launch(headless=True)

            # Abre una nueva página
            page = browser.new_page()

            # Abre la URL
            page.goto(url)

            # Realiza scraping de elementos específicos
            titulo = page.query_selector(
                "xpath=/html/body/main/div/div[1]/section[1]/div/div[1]/div/div/div/h2").inner_text()

            # Imprime los resultados
            print("Título de la página desde Playwrigh:", titulo)

            # Cierra el navegador
            browser.close()

            return titulo

    def parse_data(self, data):
        print(f"Parsing data Playwright {data}")

    def store_data(self, data):
        print(f"Saving data Playwright {data}")

