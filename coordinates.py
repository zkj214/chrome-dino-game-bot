import pyautogui


def get_coordinates():
    pyautogui.displayMousePosition()
    coor=tuple(pyautogui.position())

    return coor


xy=get_coordinates()
print(xy)