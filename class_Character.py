import random
import time
with open('data.txt', encoding="utf-8") as path:
    data = path.read().splitlines()

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

raw_descriptors = data[0].split(", ")
descriptors = []
for descriptor in raw_descriptors:
    slowa = descriptor.split()
    if len(slowa) == 2:
        descriptor = {"m": slowa[0], "d": slowa[1]}
        descriptors.append(descriptor)

raw_enemies = data[1].split(", ")
enemies = []
for enemy in raw_enemies:
    slowa = enemy.split()
    if len(slowa) == 2:
        enemy = {"m": slowa[0], "d": slowa[1]}
        enemies.append(enemy)

raw_origins = data[2].split(", ")
origins = []
for origin in raw_origins:
    slowa = origin.split()
    if len(slowa) == 2:
        origin = {"m": slowa[0], "d": slowa[1]}
        origins.append(origin)

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

#generowanie losowej nazwy przeciwnika
def random_enemy_name():
    descriptors_len = len(descriptors) -1
    enemies_len = len(enemies) -1
    origins_len = len(origins) -1

    descriptor_choice = random.randint(0,descriptors_len)
    enemy_choice = random.randint(0,enemies_len)
    origin_choice = random.randint(0,origins_len)

    enemy_m = descriptors[descriptor_choice]["m"] + " " + enemies[enemy_choice]["m"] + " " + origins[origin_choice]["m"]
    enemy_d = descriptors[descriptor_choice]["d"] + " " + enemies[enemy_choice]["d"] + " " + origins[origin_choice]["d"]
    
    #zwraca wynik w formie listy (mianownik, dopelniacz)
    enemy_name = [enemy_m, enemy_d]
    return enemy_name

#klasa Charcter do tworzenia instancji przeciwników
class Character:
    def __init__ (self, name_m, name_d, hp, max_damage, defence, speed):
        self.name_m = name_m
        self.name_d = name_d
        self.hp = hp
        self.max_damage = max_damage
        self.defence = defence
        self.speed = speed
    def przedstaw(self):
        print(f"Na arenę wkracza {self.name_m}...")
        print(f"M: {self.name_m.title()} \nD: {self.name_d.title()} \nHP:  {self.hp} \nDMG: {self.max_damage} \nDEF: {self.defence} \nSPD: {self.speed}")


def tworz_przeciwnika(enemy_modifier=1):
    enemy_name = random_enemy_name()
    enemy = Character(enemy_name[0], enemy_name[1], roll(8, 12) + enemy_modifier, 2 * roll(2,4) + enemy_modifier, 2 * roll(2,4) + enemy_modifier, roll())
    return enemy











