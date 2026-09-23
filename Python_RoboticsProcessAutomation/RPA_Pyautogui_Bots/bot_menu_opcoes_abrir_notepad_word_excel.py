import pyautogui
import pyautogui as escolha_opcao


opcao = pyautogui.confirm('Clique na opcao desejada', buttons = ['Notepad', 'Word', 'Excel'])

# primeira opcao EXCEL
if opcao == 'Excel':
  escolha_opcao.hotkey('win','r')
  escolha_opcao.sleep(2)
  escolha_opcao.write('Excel')
  escolha_opcao.sleep(2)
  escolha_opcao.press('enter')
  escolha_opcao.sleep(2)
  # print('A posicao do mouse inicialmente e' + str(escolha_opcao.position()))
  # position capturada (x=639, y=319)
  escolha_opcao.typewrite('Escolhi abrir o Excel')

# Opcao NOTEPAD
elif opcao == 'Notepad':
  escolha_opcao.hotkey('win','r')
  escolha_opcao.sleep(2)
  escolha_opcao.write('Notepad')
  escolha_opcao.sleep(2)
  escolha_opcao.press('enter')
  escolha_opcao.sleep(2)
  escolha_opcao.typewrite('Escolhi abrir o Notepad')

# Opcao WORD
elif opcao == 'Word':
  escolha_opcao.hotkey('win','r')
  escolha_opcao.sleep(2)
  escolha_opcao.write('winword')
  escolha_opcao.sleep(2)
  escolha_opcao.press('enter')
  escolha_opcao.sleep(2)
  # print('A posicao do mouse inicialmente e' + str(escolha_opcao.position()))
  # x=389, y=302
  escolha_opcao.typewrite('Escolhi abrir o Word')
