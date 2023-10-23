inventory = []

if "Da Capo" in inventory:
    print("The beauty of a silent symphony!")
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

print(inventory[4])

if "Sound of a Star" in inventory:
    print("LET US MEET AGAIN IN THE STARS!")
