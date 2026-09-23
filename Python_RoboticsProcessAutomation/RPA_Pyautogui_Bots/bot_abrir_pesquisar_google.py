import pyautogui as posicaoAbrirGoogle



print('----------------🤖🚀 Iniciando Bot abrir Google e digitar pesquisa 🤖 🚀----------------------\n')
posicaoAbrirGoogle.sleep(2)
print('A posicao do mouse inicialmente e' + str(posicaoAbrirGoogle.position()))


posicaoAbrirGoogle.doubleClick(x=1035, y=1051)
posicaoAbrirGoogle.sleep(4)
print('🤖----------------Acessando pesquisa----------------------🤖\n')
posicaoAbrirGoogle.typewrite('https://www.google.com')
posicaoAbrirGoogle.sleep(2)
posicaoAbrirGoogle.press('Enter')
posicaoAbrirGoogle.sleep(2)

print('🤖----------------Digitando  pesquisa----------------------🤖\n')
posicaoAbrirGoogle.typewrite('Thrasher Magazine')
posicaoAbrirGoogle.press('Enter')
posicaoAbrirGoogle.sleep(2)
