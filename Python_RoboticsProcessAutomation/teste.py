from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

print("Iniciando automação...")

# Inicializa o ChromeDriver automaticamente
service = Service(ChromeDriverManager().install())

options = webdriver.ChromeOptions()

# IMPORTANTE para WSL (evita alguns erros gráficos)
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get("https://www.google.com")

    time.sleep(2)

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("RPA com Python")
    search_box.send_keys(Keys.ENTER)

    time.sleep(5)

    print("Busca realizada com sucesso!")

finally:
    driver.quit()

print("Finalizado.")
