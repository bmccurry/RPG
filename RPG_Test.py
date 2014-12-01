#RPG_TEST
#Dennis Gordick
#Brandon McCurry
#10/21/2014

#file system fully works, if you don't understand how to use it ask Brandon
"""
Task list:
allow player to leave game
create different types of monsters
improve shop inventory
gain skill points every level to improve yourself
add multiple save files
"""
import random
import time
import pickle, shelve
from Enemies import Player, Monster, Shop_Keeper, Monster_Boss

class main():
    def __init__(self):
        response=self.valid_input("New game or Load game?",["load","new"])
        if response == "load":
            try:
                f = shelve.open("save.dat")
                attribute = f["attributes"]
                person = attribute[0]
                f.close()
                print("Success!")
            except:
                print("Save file is corrupt or doesn't exist")
                response="new"
        if response=="new":
            Name=input("What is your name?")
            Race=self.valid_input("What is your race? (Human, Elf, Dwarf) ", ["human","elf","dwarf"])
            #Race=input("What is your race? (Your choices are Human, Elf, and Dwarf.)")
            Class=self.valid_input("What is your class? (Warrior, Archer, Mage) ", ["warrior","archer","mage"])
            #Class=input("What is your class? (Your choices are Warrior, Archer, and Mage.")
            person = Player(Name, Race, Class)
            
        while person.health > 0:
            person.update()
            explore=self.valid_input("Do you want to explore, go to town, look at some info, or save? ", ["explore","town","save","info"])
            #explore=input("Do you want to explore or go to town or look at some stats/info or even save? (only say explore or town or info or save)")
            turns=1
            if explore=="explore":
                lvl=self.valid_int("What level monsters?")
                print("You explore")
                turns=1
                while turns < 100 and int(person.health) > 0:
                    encounter=random.randint(1,100)

                    #normal fight
                    if int(encounter) >=70:
                        enemy = Monster(lvl,person)
                        print("You encounterd a LVL: "+str(enemy.lvl)+" Monster!")
                        self.fight(person, enemy)
                        person.kills += 1

                    elif int(encounter)<70:
                        loot = random.randint(1,100)
                        trap = random.randint(1,100)

                        if int(loot)>=60:
                            person.gold=int(person.gold)+int(lvl)
                            print("You found "+str(lvl)+" gold")
                            print("You have a total of "+str(person.gold)+" gold")
                            print()
                        elif int(loot)<=10:
                            if int(trap)>=50:
                                person.health=int(person.health)-10
                                print("You step on a trap")
                                print("You lost ten health")
                                print("Your total health is "+str(person.health))
                                print()
                                          
                    if int(turns)== 100:
                        #Boss fight
                        boss=random.randint(1,10)
                        if int(boss)>5:
                            print("Boss Fight!")
                            run=self.valid_input("Do you fight or run?", ["fight","run"])
                            if run.lower() == "fight":
                                satan = Monster_Boss(lvl,person)
                                self.fight(person, satan)
                                person.boss_kills += 1
                                            
                    turns+=1
                    print("End of turn "+ str(turns)+"\n")
                    time.sleep(1.0)

            elif explore=="info":
                 print("Level",str(person.lvl))
                 print("Total kills",str(person.kills))
                 print("Total boss kills",str(person.boss_kills))
                 print("Total gold",str(person.gold))
                 print("Total potions",str(person.potions))
                 print("Total xp", str(person.xp))

            elif explore=="save":
                f = shelve.open("save.dat")
                attributes = [person]
                f["attributes"] = attributes
                f.sync()
                f.close()
                print("\nSaved!\n")

            #Going to town (giggity)
            while explore=="town":
                town=self.valid_input("Where do you want to go? (shop, inspector, blacksmith, tavern, leave)", ["shop","inspector","blacksmith","tavern","leave"])

                if town=="shop":
                    print("Your gold "+str(person.gold))
                    print("The shopkeep says 'We only have potions of health! They are 20 gold each!'")
                    bought=input("How many do you want?")
                    if bought.isdigit():
                        cost=int(bought)*20
                        if int(person.gold)>=int(cost):
                            person.potions+=int(bought)
                            person.gold-=int(cost)
                            print("Gold left "+str(person.gold))
                            print("Total potions "+str(person.potions))
                        else:
                            print("'Your to poor! Come back with some gold fool!'\nThe shopkeeper kicks you out.")
                    elif bought.strip("-").isdigit():
                        print("Aye. Trying to pull a fast one on me are ya?")
                        keep = Shop_Keeper(person, bought)
                        self.fight(person, keep)
                        if person.health > 0:
                            person.potions += int(bought)*-1
                elif town=="inspector":
                    print("Coming soon")

                elif town=="blacksmith":
                    print("Coming soon")

                elif town=="leave":
                    explore = "leave"

                while town=="tavern":
                    print("Hello traveler, what can I do for you? A drink? Or the latest rumore?")
                    bar_keep=self.valid_input("Whats your choice? (drink, rumore, or leave)", ["drink","rumore","leave"])

                    if bar_keep=="drink":
                        print("Drinks cost one gold.")
                        drink=self.valid_input("Do you want a drink? ",["yes","no"])

                        while drink=="yes" and person.gold > 0:
                            person.gold=int(person.gold)-1
                            print("Your gold: "+str(person.gold))
                            print("You get drunk out of your mind.")
                            drink = input("Another? ")
                            
                    if bar_keep=="rumore":
                        if int(person.lvl) < 20:
                            print("I don't know anything.")
                        else:
                            print("No, rumors at the moment.")

                    if bar_keep=="leave":
                        print("Goodbye")
                        town = ""

    def fight(self, person, enemy):
        while int(enemy.health) > 0 and person.health > 0:
            print("Your Health: "+str(person.health))
            print(enemy.name + " Health: "+str(enemy.health))
            attack=input("Do you attack or use a potion? ")
            #your turn
            if attack == "attack":
                hit=random.randint(1,100)
                if int(hit)<=75:
                    dmg=person.dmg()
                    enemy.health-=int(dmg)
                    print("\nYou did "+ str(dmg)+" damage")
                else:
                    print("You missed!")
            elif attack=="potion":
                if person.potions > 0:
                    person.health=90+int(person.extra_health)
                    print("Potions left... "+str(person.potions))
                else:
                    print("You have no potions... You just waisted your turn!")
            else:
                print("You sit there and take it")

            #enemies turn
            if int(enemy.health) > 0:
                if enemy.potions > 0 and enemy.health < person.dmg_min:
                    enemy.health += enemy.max_health//4
                    enemy.potions -= 1
                    print("The " + str(enemy.name) + " drank a potion")
                else:
                    monster_hit_chance=random.randint(1,100)
                    if int(monster_hit_chance)<=60:
                        person.health=int(person.health)-int(enemy.dmg)
                        print("The " + str(enemy.name) + " did "+ str(enemy.dmg)+" damage")
                        if person.health <= 0:
                            print("You died")
                    else:
                        print("The " + str(enemy.name) + " missed!")

            #loot and xp for normal monster
            else:
                person.xp+=int(enemy.xp)
                print("\nThe " + str(enemy.name) + " died\n")
                print("XP gained: "+ str(enemy.xp))
                print("Your XP: "+ str(person.xp))
                loot_chance=random.randint(1,100)
                if int(loot_chance) <10:
                    print("No loot :(")
                    print("Your gold "+str(person.gold))
                elif int(loot_chance) <90:
                    print("Your gold sir. It this many..." +str(enemy.gold))
                    if enemy.loot != "":
                        print("There was also a " + str(enemy.loot) + " on him.")
                        line = "Would you like to replace it with your " + str(person.weapon) + "? "
                        opt = self.valid_input(line, ["yes","no"])
                        if opt.lower() == "yes":
                            person.weapon = enemy.loot
                            print("Congradulations! Your new weapon is a " + str(person.weapon))
                    person.gold+=int(enemy.gold)
                    print("Your gold "+str(person.gold))
                else:
                    print("Rare loot! 1 potion!")
                    person.potions+=1
                    print("\nYour total potions "+str(person.potions))

    def valid_input(self, question, valid):
        response = input(question)
        while response.lower() not in valid:
            print("Valid responses: ")
            for i in valid:
                print(i)
            response = input(question)
        return response

    def valid_int(self, question):
        response = input(question)
        while not response.isdigit():
            print("That is not a number")
            response = input(question)
        return int(response)
            

main()

