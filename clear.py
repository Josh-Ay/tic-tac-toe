import pyautogui


def clear():
    current_x, current_y = pyautogui.position()[0], pyautogui.position()[1]
    pyautogui.click(current_x, current_y)
    pyautogui.hotkey('Ctrl', ';')
