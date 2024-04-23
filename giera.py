from class_Character import Character
from class_Character import tworz_przeciwnika
from class_Character import roll
from class_Character import wait
import time

print("Witaj w grze:")
print('''
                   ______________________________________
          ________|                                      |_______
          \       |            ARENA ŚMIERCI IV:         |      /
           \      |          Pokój nie jest drogą        |     /
           /      |______________________________________|     \\
          /__________)                                (_________\\
''')

player = Character("Gracz", "gracza", 100, 5, 8, 5)

player.przedstaw()

x = 1
z = 1

ilosc_zwyciestw = 0
pokonani_wrogowie = []

wait(2)

while True:
    input(f"Walka nr {x}.\nMasz {player.hp} pkt. życia. \nCzy jestes gotowy? (Wcisnij ENTER)")
    name = "poziom" + str(x)
    print(f"\nPrzeciwnik nr {x}:")
    enemy = tworz_przeciwnika(z)
    enemy.przedstaw()
    z += 2
    x += 1
    runda = 1
    input(f"\nCzy chcesz zaatakować {enemy.name_d}? (Wcisnij ENTER)")
    while True:
        gracz_inicjatywa = 1
        enemy_inicjatywa = 1
        while gracz_inicjatywa == enemy_inicjatywa:
            gracz_inicjatywa = player.speed * roll(1,6)
            enemy_inicjatywa = enemy.speed * roll(1,6)
        
        if gracz_inicjatywa > enemy_inicjatywa:
            print(f"\n------ Runda {runda} ------")
            time.sleep(1)
            print("Atakujesz pierwszy.")
            runda += 1
            atak = player.max_damage * roll(1,6)
            enemy.hp -= atak
            print(f"Atakujesz {enemy.name_d} i zadajesz {atak} pkt. obrażeń!")
            print(f"Życie {enemy.name_d}: {enemy.hp}")
            if enemy.hp < 1:
                ilosc_zwyciestw += 1
                pokonani_wrogowie.append(enemy.name_m.title())
                print("\nZwyciestwo!")
                print(f"Zostało Ci {player.hp} pkt. życia.")
                wait(2)
                break
            time.sleep(3)
            atak = enemy.max_damage * roll(1,6)
            player.hp -= atak
            print(f"{enemy.name_m.title()} atakuje Cie i zadaje {atak} pkt. obrażeń!")
            print(f"Życie gracza: {player.hp}")
            if player.hp < 1:
                player.hp = 0
                print("\nPorazka!")
                break
            time.sleep(3)
        else:
            print(f"\n------ Runda {runda} ------")
            time.sleep(1)
            print(f"Przeciwnik atakuje pierwszy.")
            runda += 1
            atak = enemy.max_damage * roll(1,6)
            player.hp -= atak
            print(f"{enemy.name_m.title()} atakuje Cie i zadaje {atak} pkt. obrażeń!")
            print(f"Życie gracza: {player.hp}")
            if player.hp < 1:
                print("\nPorazka!")
                break
            time.sleep(3)
            atak = player.max_damage * roll(1,6)
            enemy.hp -= atak
            print(f"Atakujesz {enemy.name_d} i zadajesz {atak} pkt. obrażeń!")
            print(f"Życie {enemy.name_m}: {enemy.hp}")
            if enemy.hp < 1:
                enemy.hp = 0
                ilosc_zwyciestw += 1
                pokonani_wrogowie.append(enemy.name_m.title())
                print("\nZwyciestwo!")
                print(f"Zostało Ci {player.hp} pkt. życia.")
                wait(2)
                break
            time.sleep(3)

    if player.hp < 1:
        print(f"Pokonał Cie {enemy.name_m.title()}!")
        print(f"\nPokonani wrogowie: {ilosc_zwyciestw} ({", ".join(pokonani_wrogowie)})")
        print("\nGAME OVER")
        break