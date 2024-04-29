from class_Character import Character
from class_Character import tworz_przeciwnika
from class_Character import roll
from class_Character import wait
from druki import loading_enemy
from druki import print_with_effect

import time
import os
clear = lambda: os.system('cls')

def player_attack():
    atak = player.max_damage * roll(0,3)
    if atak < 1:
        print(f"\n[ATAK GRACZA]")
        time.sleep(fight_speed)
        print(f"    Pudłujesz!")
    else:
        print(f"\n[ATAK GRACZA]") 
        time.sleep(fight_speed)
        if atak == player.max_damage*3:
            print("    BLOOD RAMPAGE!")
            atak = atak*3
            time.sleep(fight_speed)
        print(f"    Atakujesz {enemy.name_d} i zadajesz {atak} pkt. obrażeń!")
        enemy.hp -= atak
        time.sleep(1)
        print(f"    Życie przeciwnika: {enemy.hp}")




def enemy_attack():
    #atak przeciwnika
    atak = enemy.max_damage * roll(0,3)
    if atak < 1:
        print(f"\n[ATAK PRZECIWNIKA]")
        time.sleep(fight_speed)
        print(f"    Przeciwnik pudłuje!")
    else:
        print(f"\n[ATAK PRZECIWNIKA]")
        time.sleep(fight_speed)
        if atak == enemy.max_damage*3:
            print("    MAX DAMAGE!")
            time.sleep(fight_speed)
        print(f"    {enemy.name_m.title()} atakuje Cię i zadaje {atak} pkt. obrażeń!")
        player.hp -= atak
        time.sleep(1)
        print(f"    Życie gracza: {player.hp}")

def player_levelup():
    print(f"\nAwansujesz na poziom {x}!")
    time.sleep(1)

    hp_bonus = x + roll(1,6)
    dmg_bonus = x + roll(1,3)
    spd_bonus = x + roll(1,3)

    player.hp += hp_bonus
    print(f"Otrzymujesz premię +{hp_bonus} do punktów życia!")
    time.sleep(1)
    player.max_damage += dmg_bonus
    print(f"Otrzymujesz premię +{dmg_bonus} do ataku!")
    time.sleep(1)
    player.speed += spd_bonus
    print(f"Otrzymujesz premię +{spd_bonus} do prędkości!")
    time.sleep(1)
    print(f"{player.name_m.title()} - HP: {player.hp}, DMG: {player.max_damage}, SPD: {player.speed}")

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

fight_speed = 2
print(f"\nPrędkość walki: {fight_speed}")


player = Character(imie.title(), "gracza", "m", 100, 5, 8, 5)

print(f"\nJesteś znany jako {imie.title()} z Magicznego Zagajnika.")
time.sleep(1)
print("Trudnisz się wojaczką.")
time.sleep(1)
print("Podczas swoich podróży natrafiasz na Arenę Walk znaną w Krainach jako: ")
time.sleep(1)
print("\nArena Śmierci IV")
time.sleep(1)
input(f"\nCzy decydujesz się wkroczyć na Arenę Śmierci? (Wcisnij ENTER)")

x = 1
z = 1
ilosc_zwyciestw = 0
pokonani_wrogowie = []

while True:
    clear()
    name = "poziom" + str(x)
    enemy = tworz_przeciwnika(x)
    loading_enemy(3 , 0.03)
    print(f"Na arenę wkracza:")
    enemy.przedstaw()
    z += 2
    runda = 1
    time.sleep(fight_speed)
    input(f"\nMasz {player.hp} pkt. życia. \nCzy jestes gotowy by zaatakować {enemy.name_d}? (Wcisnij ENTER)")

    clear()
    print(f"Starcie nr {x}: {player.name_m} - (HP: {player.hp}, DMG: {player.max_damage}, SPD: {player.speed}) vs {enemy.name_m.title()} - (HP: {enemy.hp}, DMG: {enemy.max_damage}, SPD: {enemy.speed})")
    
    x += 1

    while True:
        gracz_inicjatywa = 1
        enemy_inicjatywa = 1
        while gracz_inicjatywa == enemy_inicjatywa:
            gracz_inicjatywa = player.speed * roll(1,6)
            enemy_inicjatywa = enemy.speed * roll(1,6)
        
        if gracz_inicjatywa > enemy_inicjatywa:
            print(f"\n----- Runda {runda} -----")
            time.sleep(1)
            print("\nJesteś szybszy i atakujesz pierwszy!")
            time.sleep(fight_speed)
            runda += 1

            player_attack()
            if enemy.hp < 1:
                ilosc_zwyciestw += 1
                pokonani_wrogowie.append(enemy.name_m.title())
                time.sleep(fight_speed)
                print("\nZwyciestwo!")
                time.sleep(fight_speed)
                player_levelup()
                input(f"\nMasz {player.hp} pkt. życia. \nCzy jestes gotowy by kontynuować? (Wcisnij ENTER)")
                clear()
                break
            time.sleep(fight_speed)

            enemy_attack()
            if player.hp < 1:
                player.hp = 0
                time.sleep(fight_speed)
                print("\nPorazka!")
                break
            time.sleep(fight_speed)

        else:
            print(f"\n----- Runda {runda} -----")
            time.sleep(1)
            print(f"\nPrzeciwnik jest szybszy i atakuje pierwszy.")
            time.sleep(fight_speed)
            runda += 1

            enemy_attack()
            if player.hp < 1:
                player.hp = 0
                time.sleep(fight_speed)
                print("\nPorazka!")
                break
            time.sleep(fight_speed)
            player_attack()
            if enemy.hp < 1:
                ilosc_zwyciestw += 1
                pokonani_wrogowie.append(enemy.name_m.title())
                time.sleep(fight_speed)
                print("\nZwyciestwo!")
                time.sleep(fight_speed)
                player_levelup()
                input(f"\nMasz {player.hp} pkt. życia. \nCzy jestes gotowy by kontynuować? (Wcisnij ENTER)")
                clear()
                break
            time.sleep(fight_speed)

    if player.hp < 1:
        print(f"Pokonał Cię {enemy.name_m.title()}!")
        if ilosc_zwyciestw < 1:
            print(f"\n{imie.title()}, nie udało Ci sie pokonać ani jednego przeciwnika.")
        else:
            print(f"\nGratulacje, {imie.title()}! Pokonani przeciwnicy: {ilosc_zwyciestw}!")

        time.sleep(5)
        print_with_effect("GAME OVER")
        time.sleep(1)
        print(f"Twój wynik to {ilosc_zwyciestw} zwycięstw!.")
              
        print(f"Pokonani wrogowie to: {", ".join(pokonani_wrogowie)}!")
        break