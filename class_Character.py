import random
import time
with open('data.txt', encoding="utf-8") as path:
    data = path.read().splitlines()


#PRZENIESC
#wyświetl kropki
def wait(x):
    while x > 0:
        print(".")
        time.sleep(1)
        x -= 1

#rzut kością
def roll(min=1, max=6):
    roll_result = random.randint(min, max)
    return roll_result


# #przyklad dzialania funkcji tworzacej liste ze slownikiem
# print(f"krok 1: {data}")
# raw_descriptors = data[0].split(", ")
# print(f"krok 2: {raw_descriptors}")
# descriptors = []
# for descriptor in raw_descriptors:
#     slowa = descriptor.split()
#     if len(slowa) == 2:
#         descriptor = {"m": slowa[0], "d": slowa[1]}
#         descriptors.append(descriptor)
# print(f"krok 3: {descriptors}")
# #koniec przykladu

raw_descriptors_m = data[12].split(", ")
descriptors_m = []
for descriptor in raw_descriptors_m:
    slowa = descriptor.split()
    if len(slowa) == 2:
        descriptor = {"m": slowa[0], "d": slowa[1]}
        descriptors_m.append(descriptor)

raw_descriptors_f = data[13].split(", ")
descriptors_f = []
for descriptor in raw_descriptors_f:
    slowa = descriptor.split()
    if len(slowa) == 2:
        descriptor = {"m": slowa[0], "d": slowa[1]}
        descriptors_f.append(descriptor)


raw_origins_m = data[14].split(", ")
origins_m = []
for origin in raw_origins_m:
    slowa = origin.split()
    if len(slowa) == 2:
        origin = {"m": slowa[0], "d": slowa[1]}
        origins_m.append(origin)

raw_origins_f = data[15].split(", ")
origins_f = []
for origin in raw_origins_f:
    slowa = origin.split()
    if len(slowa) == 2:
        origin = {"m": slowa[0], "d": slowa[1]}
        origins_f.append(origin)


raw_enemies_lvl1 = []
raw_enemies_lvl2 = []
raw_enemies_lvl3 = []
raw_enemies_lvl4 = []
raw_enemies_lvl5 = []
raw_enemies_lvl6 = []
raw_enemies_lvl7 = []

enemies_lvl1 = []
enemies_lvl2 = []
enemies_lvl3 = []
enemies_lvl4 = []
enemies_lvl5 = []
enemies_lvl6 = []
enemies_lvl7 = []

counter = 1
for n in range(7):
    raw_name = f"raw_enemies_lvl{counter}"
    globals()[raw_name] = data[counter+3].split(", ")
    enemies_name = f"enemies_lvl{counter}"
    #globals()[enemies_name] = []
    for enemy in globals()[raw_name]:
        slowa = enemy.split()
        if len(slowa) == 3:
            enemy = {"m": slowa[0], "d": slowa[1], "gender": slowa[2]}
            globals()[enemies_name].append(enemy)
    counter += 1

# print(f"raw_enemies_lvl1: {raw_enemies_lvl1}")
# print(f"raw_enemies_lvl2: {raw_enemies_lvl2}")
# print(f"raw_enemies_lvl3: {raw_enemies_lvl3}")
# print(f"raw_enemies_lvl4: {raw_enemies_lvl4}")
# print(f"raw_enemies_lvl5: {raw_enemies_lvl5}")
# print(f"raw_enemies_lvl6: {raw_enemies_lvl6}")
# print(f"raw_enemies_lvl7: {raw_enemies_lvl7}")
# print(f"\nenemies_lvl1: {enemies_lvl1}")
# print(f"\nenemies_lvl2: {enemies_lvl2}")
# print(f"\nenemies_lvl3: {enemies_lvl3}")
# print(f"\nenemies_lvl4: {enemies_lvl4}")
# print(f"\nenemies_lvl5: {enemies_lvl5}")
# print(f"\nenemies_lvl6: {enemies_lvl6}")
# print(f"\nenemies_lvl8: {enemies_lvl7}")


#generowanie losowej nazwy przeciwnika
def random_enemy_name(level = 1):
    choose_from = []
    if level == 1:
        choose_from = enemies_lvl1
    elif level == 2:
        choose_from = enemies_lvl2
    elif level == 3:
        choose_from = enemies_lvl3
    elif level == 4:
        choose_from = enemies_lvl4
    elif level == 5:
        choose_from = enemies_lvl5
    elif level == 6:
        choose_from = enemies_lvl6
    else:
        choose_from = enemies_lvl7

    enemies_len = len(choose_from) -1
    enemy_roll = random.randint(0,enemies_len)

    # print(choose_from[enemy_roll]["m"])
    # print(choose_from[enemy_roll]["d"])
    # print(choose_from[enemy_roll]["gender"])

    gender = choose_from[enemy_roll]["gender"]

    if gender == "m":
        descriptor_choice = descriptors_m
        origin_choice = origins_m
    else:
        descriptor_choice = descriptors_f
        origin_choice = origins_f

    descriptors_len = len(descriptor_choice) -1
    origins_len = len(origin_choice) -1

    descriptor_roll = random.randint(0,descriptors_len)
    origin_roll = random.randint(0,origins_len)

    enemy_m = descriptor_choice[descriptor_roll]["m"] + " " + choose_from[enemy_roll]["m"] + " " + origin_choice[origin_roll]["m"]
    enemy_d = descriptor_choice[descriptor_roll]["d"] + " " + choose_from[enemy_roll]["d"] + " " + origin_choice[origin_roll]["d"]
    #enemy_gender = choose_from[enemy_roll]["gender"]
    
    #zwraca wynik w formie listy (mianownik, dopelniacz)
    enemy_name = [enemy_m, enemy_d, gender]
    return enemy_name

#klasa Charcter do tworzenia instancji przeciwników
class Character:
    def __init__ (self, name_m, name_d, gender, hp, max_damage, defence, speed):
        self.name_m = name_m
        self.name_d = name_d
        self.gender = gender
        self.hp = hp
        self.max_damage = max_damage
        self.defence = defence
        self.speed = speed
    def przedstaw(self):
        print(f"{self.name_m.title()} (HP: {self.hp}, DMG: {self.max_damage}, SPD: {self.speed})")


def tworz_przeciwnika(enemy_modifier=1):
    base_hp = roll(2,6) * enemy_modifier
    base_dmg = roll(2,6) * enemy_modifier
    base_speed = roll(1,3) * enemy_modifier
    enemy_name = random_enemy_name(enemy_modifier)
    enemy = Character(enemy_name[0], enemy_name[1], enemy_name[2], base_hp + 2*roll(1,4), base_dmg + 2*roll(1,4), 1, base_speed + 2*roll(1,4))
    return enemy

print(f"\nLosowi przeciwnicy:")
i = 1
while i < 8:
    przecio = tworz_przeciwnika(i)
    #print(f"Level {i}: {przecio}")
    przecio.przedstaw()
    i += 1










