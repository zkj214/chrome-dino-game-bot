import pyautogui
import time


class Coordinates:
    def __init__(self):
        # coordinates of replay button to start the game
        self.replaybutton = (360, 214)


coordinates=Coordinates()


def restartGame():
    # using pyauto gui library, we are clicking on the
    # replay button without any user interaction
    pyautogui.click(coordinates.replaybutton)


def press_space():
    # releasing the  Down Key
    pyautogui.keyUp('down')

    # pressing Space to overcome Bush
    pyautogui.keyDown('space')

    # so that Space Key will be recognized easily
    time.sleep(0.05)

    # printing the "Jump" statement on the
    # terminal to see the current output
    print("jump")
    time.sleep(0.10)

    # releasing the Space Key
    pyautogui.keyUp('space')

    # again pressing the Down Key to keep my Bot always down
    pyautogui.keyDown('down')


restartGame()
while True:
    img=pyautogui.screenshot()
    screen=img.getpixel((408, 524))
    x1=img.getpixel((227, 589))
    x2=img.getpixel((273, 767))
    x3=img.getpixel((205, 767))

    if screen[0]==32:
        if x1[0]!=32 or x2[0]!=32 or x3[0]!=32:
            press_space()