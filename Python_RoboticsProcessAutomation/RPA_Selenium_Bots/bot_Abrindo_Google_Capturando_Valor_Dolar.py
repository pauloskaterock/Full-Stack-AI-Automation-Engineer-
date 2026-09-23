from selenium import webdriver  as opcao_selenium
from selenium.webdriver.common.keys import Keys
import pyautogui as tempoPausaComputador
from selenium.webdriver.common.by import By

meuNavegador = opcao_selenium.Chrome()
print("Bot Abrindo Navegador ------------------------------------------")
meuNavegador.get("https://www.google.com")
tempoPausaComputador.sleep(4)

meuNavegador.find_element(By.NAME, "q").send_keys("Cotacao Dolar")
tempoPausaComputador.sleep(4)

meuNavegador.find_element(By.NAME, "q").send_keys(Keys.RETURN)
tempoPausaComputador.sleep(4)


valorDolarPeloGoogle = meuNavegador.find_elements(By.XPATH, "/html/body/div[2]/div[6]/form/div[1]/div/div[4]/center/input[1]")[0].text
tempoPausaComputador.sleep(4)
print(f"O valor do dólar é: {valorDolarPeloGoogle}")
