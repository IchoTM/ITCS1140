#Currently does not work and welp i feel like shit so im not making it work rn#
player = {"HP" : 100 , "Attack" : 10 , "Heal" : 4}
enemy = {"HP" : 100 , "Attack" : 11}
def pAtk(e,p):
    en = e
    pl = p
    en["HP"] - pl["Attack"]
    return en["HP"]
    print("en hp = " + str(en["HP"]))
def eAtk(e,p):
    en = e
    pl = p
    pl["HP"] - en["Attack"]
    print("playe health = " + str(pl["HP"]))
    return pl["HP"]
def pHel(p):
    player["HP"] + 4

def game(p,e):
    pl = p
    en = e
    print("This is a super simple turnbased game")
    while pl["HP"] > 0:
        ui = int(input("Do you want to 1) Attack 2) Heal 3) Check Remaining Heals : "))
        if ui == 1:
            print("1")
            en["HP"] = pAtk(en,pl)
            pl["HP"] = eAtk(en,pl)
        elif ui == 2:
            pHel()
        elif ui == 3:
            print(player["Heal"])
        else:
            print("That wasn't an option and now you wasted a turn")
            pl["HP"] = eAtk(en,pl)
        print("HP Remaining " + str(player["HP"]))
        print
        if enemy["HP"] == 0:
              print("YOU WON!")
              player["HP"] = 0

def main():
    game(player,enemy)

main()
