import random

with open('data.txt', encoding="utf-8") as path:
    data = path.read().splitlines()



#przyklad dzialania funkcji tworzacej liste ze slownikiem
print(f"krok 1: {data}")
raw_descriptors = data[0].split(", ")
print(f"krok 2: {raw_descriptors}")
descriptors = []
for descriptor in raw_descriptors:
    slowa = descriptor.split()
    if len(slowa) == 2:
        descriptor = {"m": slowa[0], "d": slowa[1]}
        descriptors.append(descriptor)
print(f"krok 3: {descriptors}")
#koniec przykladu

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

def random_enemy_name():
    descriptors_len = len(descriptors) -1
    enemies_len = len(enemies) -1
    origins_len = len(origins) -1

    descriptor_choice = random.randint(0,descriptors_len)
    enemy_choice = random.randint(0,enemies_len)
    origin_choice = random.randint(0,origins_len)

    enemy_m = descriptors[descriptor_choice]["m"] + " " + enemies[enemy_choice]["m"] + " " + origins[origin_choice]["m"]
    enemy_d = descriptors[descriptor_choice]["d"] + " " + enemies[enemy_choice]["d"] + " " + origins[origin_choice]["d"]
    
    #wyswietla wygenerowane nazwy w zdaniu
    print(f"\nStoi przed Tobą {enemy_m}. \nAtakujesz {enemy_d}!")
    
    #zwraca wynik w formie listy (mianownik, dopelniacz)
    enemy_name = [enemy_m, enemy_d]
    return enemy_name

for i in range(5):
    random_enemy_name()


enemy_name = random_enemy_name()
print(enemy_name[0])
print(enemy_name[1])












