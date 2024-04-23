from class_Character import Character
from class_Character import tworz_przeciwnika
from class_Character import roll
from class_Character import wait
import time
import os
clear = lambda: os.system('cls')

clear()
print("Witaj w grze:")
print('''
                   ______________________________________
          ________|                                      |_______
          \       |            ARENA ŚMIERCI IV:         |      /
           \      |          Pokój nie jest drogą        |     /
           /      |______________________________________|     \\
          /__________)                                (_________\\
''')
imie = str(input("Podaj swoje imię: "))

options = input("Podaj szybkość walki 1, 2, 3): ")
if options == 1:
    fight_speed = 1
elif options == 2:
    fight_speed = 2
elif options == 3:
    fight_speed = 3
else:
    fight_speed = 2
print(f"Prędkość walki: {fight_speed}")


player = Character(imie.title(), "gracza", 100, 5, 8, 5)

print(f"\nJesteś znany jako {imie.title()} z Magicznego Zagajnika.")
time.sleep(1)
print("Trudnisz się wojaczką.")
time.sleep(1)
print("Podczas swoich podróży natrafiasz na Arenę Walk znaną w Krainach jako: ")
wait(2)
print("ARENA ŚMIERCI")
wait(2)
input(f"\nCzy decydujesz się wkroczyć na Arenę Śmierci? (Wcisnij ENTER)")

x = 1
z = 1
ilosc_zwyciestw = 0
pokonani_wrogowie = []

while True:
    clear()
    name = "poziom" + str(x)
    enemy = tworz_przeciwnika(z)
    enemy.przedstaw()
    z += 2
    runda = 1
    time.sleep(1)
    input(f"\nMasz {player.hp} pkt. życia. \nCzy jestes gotowy by zaatakować {enemy.name_d}? (Wcisnij ENTER)")

    clear()
    print(f"Starcie nr {x}: {player.name_m} vs {enemy.name_m}!")

    x += 1
    while True:
        gracz_inicjatywa = 1
        enemy_inicjatywa = 1
        while gracz_inicjatywa == enemy_inicjatywa:
            gracz_inicjatywa = player.speed * roll(1,6)
            enemy_inicjatywa = enemy.speed * roll(1,6)
        
        if gracz_inicjatywa > enemy_inicjatywa:
            print(f"\n------ Runda {runda} ------")
            time.sleep(1)
            print("\nJesteś szybszy i atakujesz pierwszy!")
            time.sleep(fight_speed)
            runda += 1
            atak = player.max_damage * roll(1,6)
            enemy.hp -= atak
            print(f"\nAtakujesz {enemy.name_d} i zadajesz {atak} pkt. obrażeń!")
            print(f"Życie {enemy.name_d}: {enemy.hp}")
            if enemy.hp < 1:
                ilosc_zwyciestw += 1
                pokonani_wrogowie.append(enemy.name_m.title())
                print("\nZwyciestwo!")
                time.sleep(fight_speed)
                input(f"\nMasz {player.hp} pkt. życia. \nCzy jestes gotowy by kontynuować? (Wcisnij ENTER)")
                clear()
                break
            time.sleep(fight_speed)
            atak = enemy.max_damage * roll(1,6)
            player.hp -= atak
            print(f"\n{enemy.name_m.title()} atakuje Cie i zadaje {atak} pkt. obrażeń!")
            print(f"Życie gracza: {player.hp}")
            if player.hp < 1:
                player.hp = 0
                print("\nPorazka!")
                break
            time.sleep(fight_speed)
        else:
            print(f"\n------ Runda {runda} ------")
            time.sleep(1)
            print(f"\nPrzeciwnik jest szybszy i atakuje pierwszy.")
            time.sleep(fight_speed)
            runda += 1
            atak = enemy.max_damage * roll(1,6)
            player.hp -= atak
            print(f"\n{enemy.name_m.title()} atakuje Cie i zadaje {atak} pkt. obrażeń!")
            print(f"Życie gracza: {player.hp}")
            if player.hp < 1:
                print("\nPorazka!")
                break
            time.sleep(fight_speed)
            atak = player.max_damage * roll(1,6)
            enemy.hp -= atak
            print(f"\nAtakujesz {enemy.name_d} i zadajesz {atak} pkt. obrażeń!")
            print(f"Życie {enemy.name_m}: {enemy.hp}")
            if enemy.hp < 1:
                enemy.hp = 0
                ilosc_zwyciestw += 1
                pokonani_wrogowie.append(enemy.name_m.title())
                print("\nZwyciestwo!")
                input(f"\nMasz {player.hp} pkt. życia. \nCzy jestes gotowy by kontynuować? (Wcisnij ENTER)")
                clear()
                break
            time.sleep(fight_speed)

    if player.hp < 1:
        print(f"Pokonał Cie {enemy.name_m.title()}!")
        print(f"\nPokonani wrogowie: {ilosc_zwyciestw} ({", ".join(pokonani_wrogowie)})")
        print("\nGAME OVER")
        break