import pyautogui

import pyautogui
import random
import time

# Включаем защиту: если увести мышь в левый верхний угол — программа остановится
pyautogui.FAILSAFE = True

# Получаем размер экрана
screen_width, screen_height = pyautogui.size()

while True:
    # Случайные координаты в пределах экрана
    x = random.randint(0, screen_width)
    y = random.randint(0, screen_height)

    # Перемещаем курсор (0.5 секунды — плавность)
    pyautogui.moveTo(x, y, duration=0.5)

    # Пауза между движениями
    time.sleep(8)

