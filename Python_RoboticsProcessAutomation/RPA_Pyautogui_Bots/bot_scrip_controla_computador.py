import pyautogui as posicaoMouse


posicaoMouse.sleep(2)
print(posicaoMouse.position())

posicaoMouse.moveTo(x=612, y=1048)
posicaoMouse.sleep(2)
 # posicaoMouse.click(x=573, y=1051)
posicaoMouse.doubleClick(x=612, y=1048)
posicaoMouse.sleep(2)


posicaoMouse.typewrite('Bloco de notas')

posicaoMouse.press('enter')
