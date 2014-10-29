import pickle, shelve

f = shelve.open("save.dat")
gold = 2
potions = "3"
f["attributes"] = {"gold": gold, "potions": potions}
f.sync()
f.close()

f = shelve.open("save.dat")
attributes = f["attributes"]
f.close()
gold = attributes["gold"]
print(gold)