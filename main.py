import pyautogui, time, random

time.sleep(10)
pyautogui.FAILSAFE = False

roundCounter = 3601

while True:

    randInt = random.randint(15, 20)
    randSec = randInt / 100

    if roundCounter > 3600:
        pyautogui.typewrite('/work', randSec)
        time.sleep(randSec)
        pyautogui.press('enter')
        time.sleep(randSec)
        pyautogui.press('enter')
        roundCounter = 0

    pyautogui.typewrite('/dice 100 ', randSec)
    time.sleep(randSec)
    pyautogui.press('enter')
    time.sleep(randSec)
    pyautogui.press('enter')
    time.sleep(randInt)
    roundCounter = roundCounter + randInt
