import xlsxwriter
import os


nomeCaminhoArquivo =  'C:\Automation-Challenges\Robos_Diversos\outRobos\Euro-Dolar-Google.xlsx'
planilhaCriada = xlsxwriter.Workbook(nomeCaminhoArquivo) # criando a planilha
sheet1 = planilhaCriada.add_worksheet()

# escrevendo nas celulas

sheet1.write("A1","Nome")
sheet1.write("B1","Idade")
sheet1.write("A2","Amanda")
sheet1.write("B2",28)
sheet1.write("A3","Roberto")
sheet1.write("B3",25)


planilhaCriada.close()

os.startfile(nomeCaminhoArquivo)
