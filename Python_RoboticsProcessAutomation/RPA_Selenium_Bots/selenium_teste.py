from selenium import webdriver


abrir_navegador = webdriver.Chrome()
print("----Bot Abrindo Navegador")

abrir_navegador.get("https://www.google.com")
