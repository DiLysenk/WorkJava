import cv2
import time
import numpy as np
import pyautogui
from PIL import ImageGrab


# search screen position, coordinates x,y
def search_screen_position(t):
    time.sleep(0.1)
    template = cv2.imread(t, 0)
    w, h = template.shape[::-1]
    # инвертируем
    # Скрин Объекта на котором находим объект
    base_screen = ImageGrab.grab(bbox=(0, 0, 1920, 1080))
    base_screen.save('1.png')

    # преобразование в cv2 формат
    img_rgb = cv2.imread('1.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)  # преобразование в читабельный формат

    # поиск скриншота
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)

    loc = np.where(res >= 0.95)  # ХЗ,
    for pt in zip(*loc[::-1]):
        x = int(pt[0])
        y = int(pt[1])

    print(x)
    print(y)
    find_screen = ImageGrab.grab(bbox=(x, y, x + w, y + w))
    find_screen.save('3.png')
    time.sleep(0.1)
    return x, y

# # найти кнопку добавить пост
# x, y = search_screen_position('1.Dobavit_bort.png')
# pyautogui.leftClick(x + 25, y + 25)
#
# # Клик по полю "Введите номер"
# x, y = search_screen_position('2.1Vvesti_nomer.png')
# pyautogui.leftClick(x + 5, y + 5)
#
# # ввести в поле "Введите номер" 1, 2
# x, y = search_screen_position('number_1.png')
# pyautogui.leftClick(x + 5, y + 5)
# x, y = search_screen_position('number_2.png')
# pyautogui.leftClick(x + 5, y + 5)
#
# # Нажать кнопку "Да"
# x, y = search_screen_position('3.knopka_da.png')
# pyautogui.leftClick(x + 5, y + 5)
#
# # Нажать кнопку "Нажать Уголок "
# x, y = search_screen_position('5.knopka_vibora.png')
# pyautogui.leftClick(x + 5, y + 5)
#
# # Нажать кнопку "Нажать Уголок "
# x, y = search_screen_position('6.nagat_trenager.png')
# pyautogui.leftClick(x + 5, y + 5)
#
# # Нажать кнопку "Подключить"
# x, y = search_screen_position('4.knopka_podkluchit.png')
# pyautogui.leftClick(x + 10, y + 10)

# Нажать кнопку "Подключить"
x, y = search_screen_position('7.na_knopku_samolet.png')
pyautogui.leftClick(x + 25, y + 25)




