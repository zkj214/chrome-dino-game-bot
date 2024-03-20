import pyautogui


def get_coordinates():
    pyautogui.displayMousePosition()
    coor=tuple(pyautogui.position())

    return coor


print(get_coordinates())