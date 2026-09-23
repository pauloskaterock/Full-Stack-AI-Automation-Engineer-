# from selenium import webdriver  as opcao_selenium
# from selenium.webdriver.common.keys import Keys
# import pyautogui as tempoPausaComputador
# import pyautogui as atalhosTeclaTeclado
# from selenium.webdriver.common.by import By

# meuNavegador = opcao_selenium.Chrome()
# print("Bot Abrindo Navegador ------------------------------------------")
# meuNavegador.get("https://www.google.com")
# tempoPausaComputador.sleep(6)

# meuNavegador.find_element(By.NAME, "q").send_keys("Cotacao Dolar")
# tempoPausaComputador.sleep(6)

# meuNavegador.find_element(By.NAME, "q").send_keys(Keys.RETURN)
# tempoPausaComputador.sleep(8)



# valorDolarPeloGoogle = meuNavegador.find_elements(By.XPATH, "/html/body/div[2]/div[6]/form/div[1]/div/div[4]/center/input[1]")[0].text
# tempoPausaComputador.sleep(4)
# print(f"O valor do dólar é: {valorDolarPeloGoogle}")


# # -----------------------------------------------------



# tempoPausaComputador.sleep(4)
# meuNavegador.find_element(By.NAME, "q").send_keys("")
# tempoPausaComputador.sleep(4)

# atalhosTeclaTeclado.press("tab")
# tempoPausaComputador.sleep(4)


# atalhosTeclaTeclado.press("enter")
# tempoPausaComputador.sleep(4)

# meuNavegador.find_element(By.NAME, "q").send_keys("Euro")
# tempoPausaComputador.sleep(4)

# meuNavegador.find_element(By.NAME, "q").send_keys(Keys.RETURN)
# tempoPausaComputador.sleep(4)



# valorEuroPeloGoogle = meuNavegador.find_elements(By.XPATH, "/html/body/div[2]/div[6]/form/div[1]/div/div[4]/center/input[1]")[0].text
# tempoPausaComputador.sleep(4)
# print(f"O valor do dólar é: {valorEuroPeloGoogle}")


# # -----------------------------Criando Excel----------------------------------

# import xlsxwriter
# import os


# nomeCaminhoArquivo =  'C:\Automation-Challenges\Robos_Diversos\outRobos\Imprimi-Euro-Dolar.xlsx'
# planilhaCriada = xlsxwriter.Workbook(nomeCaminhoArquivo) # criando a planilha
# sheet1 = planilhaCriada.add_worksheet()

# # escrevendo nas celulas

# sheet1.write("A1","Dolar")
# sheet1.write("B1","Euro")
# sheet1.write("A2",valorDolarPeloGoogle)
# sheet1.write("B2",valorEuroPeloGoogle)

#Substituir a vírgula por ponto deixando 5,38 para 5.38
# valorDolarPeloGoogle = valorDolarPeloGoogle.replace(',','.')
# valorEuroPeloGoogle = valorEuroPeloGoogle.replace(',','.')

# #Convertendo o valor do Dolar e Euro de String para Float
# valor_Dolar_Tipo_Float = float(valorDolarPeloGoogle)
# Valor_Euro_Tipo_Float = float(valorEuroPeloGoogle)

# sheet1.write("A3", valor_Dolar_Tipo_Float)
# sheet1.write("B3", Valor_Euro_Tipo_Float)

# planilhaCriada.close()

# os.startfile(nomeCaminhoArquivo)



# --------------------------------------------------------------------

#Importamos o selenium para trabalhar com as páginas da web
from selenium import webdriver as opcoes_selenium_aula
from selenium.webdriver.common.keys import Keys

#Importando a biblioteca do pyautogui para trabalhar com o tempo e teclas teclado
import pyautogui as tempoPausaComputador

#Usando o pyautogui para controlar as teclas do teclado
import pyautogui as teclasAtalhoTeclado

#Usando o By para trabalhar com as atualizações mais recentes
from selenium.webdriver.common.by import By

#Passamos autorização ao acesso as configurações do Chrome
meuNavegador = opcoes_selenium_aula.Chrome()
meuNavegador.get("https://www.google.com.br/")

#Aguarda 4 segundo para dar tempo do computador processar as informações
tempoPausaComputador.sleep(4)

#Procurando pelo elemento NAME e quando encontrar vou escrever Dolar hoje
meuNavegador.find_element(By.NAME, "q").send_keys("Dolar hoje")

#Aguarda 4 segundo para dar tempo do computador processar as informações
tempoPausaComputador.sleep(4)

#Retorna para o campo name q
#Faz a busca do valor que está digitado no campo NAME q
meuNavegador.find_element(By.NAME, "q").send_keys(Keys.RETURN)

#Aguarda 4 segundo para dar tempo do computador processar as informações
tempoPausaComputador.sleep(4)

#No resultado da pesquisa pegamo o XPATH e no meios pegamos o primeiro elemento da lista
valorDolarPeloGoogle = meuNavegador.find_elements(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')[0].text

#Aguarda 4 segundo para dar tempo do computador processar as informações
tempoPausaComputador.sleep(4)

print(valorDolarPeloGoogle)

#-----------------------------------------------------------------

#Aguarda 2 segundo para dar tempo do computador processar as informações
tempoPausaComputador.sleep(2)

#Retorna para o campo name q
#Faz a busca do valor que está digitado no campo NAME q
meuNavegador.find_element(By.NAME, "q").send_keys("")

#Aguarda 4 segundo para dar tempo do computador processar as informações
tempoPausaComputador.sleep(4)

#Estamos usando o pyautogui para apertar a tecla TAB
teclasAtalhoTeclado.press('tab')

#Aguarda 4 segundo para dar tempo do computador processar as informações
tempoPausaComputador.sleep(4)

#Estamos usando o pyautogui para apertar a tecla enter
#Enter para limpar o campo de pesquisa
teclasAtalhoTeclado.press('enter')

#Aguarda 4 segundo para dar tempo do computador processar as informações
tempoPausaComputador.sleep(4)

#Procurando pelo elemento NAME e quando encontrar vou escrever Dolar hoje
meuNavegador.find_element(By.NAME, "q").send_keys("Euro")

#Aguarda 4 segundo para dar tempo do computador processar as informações
tempoPausaComputador.sleep(4)

#Retorna para o campo name q
#Faz a busca do valor que está digitado no campo NAME q
meuNavegador.find_element(By.NAME, "q").send_keys(Keys.RETURN)

#Aguarda 4 segundo para dar tempo do computador processar as informações
tempoPausaComputador.sleep(4)

#No resultado da pesquisa pegamo o XPATH e no meios pegamos o primeiro elemento da lista
valorEuroPeloGoogle = meuNavegador.find_elements(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')[0].text

#Aguarda 4 segundo para dar tempo do computador processar as informações
tempoPausaComputador.sleep(4)

print(valorEuroPeloGoogle)

#-------------------------------------

import xlsxwriter
import os

nomeCaminhoArquivo = "A:\\Python RPA\\Extraindo Valor do Dolar e Euro e Salvando no Excel\\Imprime Dolar e Euro.xlsx"
planilhaCriada = xlsxwriter.Workbook(nomeCaminhoArquivo)
sheet1 = planilhaCriada.add_worksheet()

#Escrevendo nas células
sheet1.write("A1", "Dolar")
sheet1.write("B1", "Euro")
sheet1.write("A2", valorDolarPeloGoogle)
sheet1.write("B2", valorEuroPeloGoogle)

#Substituir a vírgula por ponto deixando 5,38 para 5.38
valorDolarPeloGoogle = valorDolarPeloGoogle.replace(',','.')
valorEuroPeloGoogle = valorEuroPeloGoogle.replace(',','.')

#Convertendo o valor do Dolar e Euro de String para Float
valor_Dolar_Tipo_Float = float(valorDolarPeloGoogle)
Valor_Euro_Tipo_Float = float(valorEuroPeloGoogle)

sheet1.write("A3", valor_Dolar_Tipo_Float)
sheet1.write("B3", Valor_Euro_Tipo_Float)

#Fechando o arquivo do Excel que está em segundo plano
planilhaCriada.close()

#Abro o arquivo
os.startfile(nomeCaminhoArquivo)
