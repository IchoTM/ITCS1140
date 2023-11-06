ego = ["EGO",["Solem Lament" ,1 , 0.5 , 1 ,2], ["Mimicry", 1, 3 , 2 ,1], ["Justitia", 2 , 2 , 2 , 2]]

##print(ego)
###expecting entire list
##print(ego[1])
###expecting all of mimicry
##print(ego[1][1])
###expecting only mimicry damage numbers
##print(ego[1][1][1])
###expecting second damage number only

def egoF(e):
    
    for entry in e:
        print(str(e[0]) + " " + str(entry))

def egoM(e):
    l = e
    c = 0
    new = []
    ui = input("Enter the name of your EGO : ")
    new.append(ui)
    while c <= 3:
        ui = input("Enter a damge number : ")
        new.append(ui)
        c += 1
    print(new)
    l.append(new)
    return l

def egoE(e):
    l = e
    i1 = int(input("Enter the first index to find your EGO : "))
    i2 = int(input("Enter the second index to find your EGO : "))
    v = input("Enter what the value should be set to : ")
    if i2 != 0:
        int(v)
    l[i1][i2] = v
    return l
def main(e):
    ui = int(input("Are you 1) Entering 2) Looking For 3) Editing an EGO? : "))
    if ui == 1:
        e = egoM(e)
        print(e)
    elif ui == 2:
        egoF(e)
    elif ui == 3:
        e = egoE(e)
    else:
        print("That Wasn't a choice")
    print(e)

main(ego)
