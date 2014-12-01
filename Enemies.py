import random
class Player():
    def __init__(self, name, race, Class):
        self.name = name
        self.race = race
        self.Class = Class
        self.potions = 0
        self.gold = 0
        self.lvl = 1
        self.xp = 0
        self.extra_health = self.lvl*10
        self.health = 90+self.extra_health
        self.max_health = self.health
        self.dmg_min = self.lvl
        self.dmg_max = self.lvl*6
        self.kills = 0
        self.boss_kills = 0
        if self.Class=="Warrior":
            self.weapon = "Sword"
        elif self.Class=="Archer":
            self.weapon=="Bow"
        else:
            self.weapon="Staff"
        print("A " + self.weapon + " is your weapon.")
        print("The "+str(self.weapon)+" weilding "+ str(self.Class)+" of the "+ str(self.race)+" clan, went out on an adventure. There name was "+str(self.name)) 

    def dmg(self):
        return random.randint(self.dmg_min, self.dmg_max)

    def update(self):
        lvl_xp = 90 + int(self.extra_health)
        while int(self.xp) >= int(lvl_xp):
            self.lvl+=1
            print("Level Up! " + str(self.lvl))
            self.dmg_min = self.lvl
            self.dmg_max = self.lvl*6
            self.extra_health = self.lvl*10
            self.health = 90+self.extra_health
            self.max_health = self.health
            lvl_xp = 90 + int(self.extra_health)
    
class Monster():
    def __init__(self, lvl, player):
        self.lvl = int(lvl)
        self.dmg = int(lvl)
        self.xp = int(lvl)//int(player.lvl)*2
        self.gold = random.randint(int(lvl)//2,int(lvl)*2)
        self.name = "Monster"
        self.health = lvl*2
        self.max_health = self.health
        self.heal = lvl*10
        self.potions = 0
        lootable = random.randint(1,100)
        if lootable > 90:
            self.loot = random.choice(["Sword","Dagger","Staff"])
        else:
            self.loot = ""
class Shop_Keeper():
    def __init__(self, player, potions):
        potions = int(potions)*-1
        self.lvl = potions*10
        self.dmg = potions*10
        self.xp = self.lvl//int(player.lvl)*2
        self.gold = potions*10+int(player.lvl)*2
        self.name = "Shop Keeper"
        self.health = self.lvl*2
        self.max_health = self.health
        self.loot = "Dagger"
        self.potions = potions

class Monster_Boss():
    def __init__(self, lvl, player):
        self.lvl = lvl
        self.dmg = lvl*3
        self.xp = lvl//player.lvl*6
        self.gold = lvl*100
        self.name = "Boss"
        self.health = player.health
        self.max_health = self.health
        self.loot = random.choice(["Battle Axe", "Club"])
        self.potions = 0


