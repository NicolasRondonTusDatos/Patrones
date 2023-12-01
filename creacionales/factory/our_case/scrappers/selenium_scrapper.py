from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

class SeleniumScraper:


    def fetch_data(self, url:str) -> str:
        options = Options()
        options.add_argument("--headless")
        # Inicializa el navegador
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        # Abre la página web
        driver.get(url)

        # Realiza scraping de elementos específicos
        # Por ejemplo, obtener el título de la página
        titulo = driver.find_element(By.XPATH, "/html/body/main/div/div[1]/section[1]/div/div[1]/div/div/div/h2").text

        # Otras acciones de scraping pueden ir aquí

        # Imprime los resultados
        print("Título de la página desde Selenium:", titulo)

        # Cierra el navegador
        driver.quit()
        return titulo

    def parse_data(self, data):
        print(f"Parsing data Selenium {data}")

    def store_data(self, data):
        print(f"Saving data Selenium {data}")


