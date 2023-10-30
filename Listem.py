inventory = []

if "Sound of a Star" in inventory:
    ("LET US MEET AGAIN IN THE STARS!")
else:
    print("Go get some E.G.O's nerd")
    
inventory = ["Mimicry", "Solem Lament", "Da Capo",
             "Seventh Bullet"]

if "Da Capo" in inventory:
    print("The beauty of a silent symphony!")
else:
    print("Go get some E.G.O's nerd")
    
print(inventory[3])

inventory.append("Sound of a Star")

print(inventory)

if "Sound of a Star" in inventory:
    print("LET US MEET AGAIN IN THE STARS!")

inventory.append("23")
inventory.sort()
print(inventory)
inventory.reverse()
print(inventory)
print(inventory.count("Mimicry"))
print(inventory.index("Sound of a Star"))
inventory.insert(3, "[CENSORD]")
print(inventory.index("[CENSORD]"))
print(inventory)
inventory.remove("[CENSORD]")
print(inventory)

inner_ego = []
inner_ego = ["Fifth Force" , "Repressed EGO"]
inventory += inner_ego
print(inventory)

inventory.sort()
inventory.reverse()
print(inventory)
inventory[3:6] = ["Corruptive E.G.O."]
print(inventory)
