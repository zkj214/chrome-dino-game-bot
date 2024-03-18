from PIL import ImageGrab, ImageOps
import pyautogui
import time
import numpy


class Coordinates:
    def __init__(self):
        # coordinates of replay button to start the game
        self.replaybutton = (360, 214)
        # this coordinates represent the top-right coordinates
        # that will be used to define the front box
        self.dinosaur = (149, 239)


coordinates=Coordinates()


def restartGame():
    # using pyautogui library, we are clicking on the
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


def imageGrab():
    # defining the coordinates of box in front of dinosaur
    box = (coordinates.dinosaur[0] + 30, coordinates.dinosaur[1],
           coordinates.dinosaur[0] + 120, coordinates.dinosaur[1] + 2)

    # grabbing all the pixels values in form of RGB tuples
    image = ImageGrab.grab(box)

    # converting RGB to Grayscale to
    # make processing easy and result faster
    grayImage = ImageOps.grayscale(image)

    # using numpy to get sum of all grayscale pixels
    a_list = numpy.array(grayImage.getcolors()) 

    # returning the sum
    print(sum(a_list))
    return a_list.sum()


# function to restart th e game
restartGame()
while True:
    # 435 is the sum of white pixels values of box.
    # You may get different value if you are taking bigger
    # or smaller box than the box taken in this article.
    # if value returned by "imageGrab" function is not equal to 435,
    # it means either bird or bush is  coming towards dinosaur
    if (imageGrab() != 435):
        press_space()