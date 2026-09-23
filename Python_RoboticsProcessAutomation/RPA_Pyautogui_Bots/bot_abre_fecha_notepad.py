import pyautogui as posicaoAbrirArquivo


print('🤖----------------Iniciando Bot abre-fecha Notepad----------------------🤖\n')
posicaoAbrirArquivo.alert('Processo iniciado! Não mexa no computador.')

print('------------------------------------------------')

print('🤖----------------Pressionando teclas----------------------🤖\n')
posicaoAbrirArquivo.hotkey('win', 'r')
posicaoAbrirArquivo.sleep(2)
posicaoAbrirArquivo.typewrite('notepad')
posicaoAbrirArquivo.press('enter')

print('🤖----------------Escrevendo no Notepad----------------------🤖\n')
posicaoAbrirArquivo.sleep(2)
posicaoAbrirArquivo.typewrite('Eu sou um Bot🤖')


# posicaoAbrirArquivo.sleep(2)
fecharJanela = posicaoAbrirArquivo.getActiveWindow()
fecharJanela.close()


posicaoAbrirArquivo.sleep(2)
posicaoAbrirArquivo.press('tab')
posicaoAbrirArquivo.sleep(2)
posicaoAbrirArquivo.press('enter')
