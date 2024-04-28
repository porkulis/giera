import time
import os
clear = lambda: os.system('cls')

def loading_enemy(occurences = 3, speed = 0.03):
    off = " "
    on = "."
    left = 0
    right = 0
    intro = "Generowanie przeciwnika: "
    for n in range(occurences):
        while left < 20:
            print(intro + off * left + on + off * right)
            left += 1
            time.sleep(speed)
            clear()
        while left > 0:
            print(intro + off * left + on + off * right)
            left -= 1
            time.sleep(speed)
            clear()


def print_with_effect(text = "Game Over"):
    lista = list(text)
    print(lista)
    off = " "
    intro = ""
    left = 10
    licznik = 0

    for n in lista:
        for n in range(10):
            print(intro + off * left + lista[licznik])
            left -= 1
            time.sleep(0.03)
            clear()
        left = 10
        intro += lista[licznik]
        licznik += 1

    print(intro)
