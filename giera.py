from slownik import Character
from slownik import tworz_przeciwnika

player = Character("Gracz", "gracza", 50, 10, 10, 5)

player.przedstaw()

x = 1
z = 1
while x < 4:
    name = "poziom" + str(x)
    print(f"\nPrzeciwnik nr {x}:")
    enemy = tworz_przeciwnika(z)
    enemy.przedstaw()
    x += 1
    z += 2