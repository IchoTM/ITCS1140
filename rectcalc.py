#pre: 
#post: returns araP value
def araP(SideNum,Leng,Rad):
    araP = (SideNum/2) * Leng * Rad
    return araP
#pre: 
#post: returns araP value
def perimP(SideNum,Leng):
    perimP = SideNum * Leng
    return perimP
#pre: 
#post: returns side num value
def getSideNums():
    SidNum = int(input("Give me your number of sides: "))
    return SidNum
#pre: 
#post: returns base value
def getBase():
    base = float(input("Give me a base: "))
    return base
#pre: 
#post: returns height value
def getHeig():
    height = float(input("Give me a height: "))
    return height
#pre: requires base and height values
#post: returns area value
def araT(b,h):
    area = (b * h)/2
    return area
#pre: 
#post: returns length value
def getLeng():
    length = float(input("Give me the length: "))
    return length
#pre: 
#post: returns width value
def getWidt():
    width = float(input("Give me the width: "))
    return width
#pre: 
#post: returns radius value
def getRad():
    rad = float(input("Give me the radius of the inscribed circle: "))
    return rad
#pre: requires length and width values
#post: returns area value
def ara(l,w):
    area = l * w
    return area
#pre: requires length and width values
#post: returns perimeter value
def perim(l,w):
    perimeter = 2 * (l + w)
    return perimeter
#pre: requires area and perimeter values
#post: calculates displays area and perimeter for rectangles
def triCalc():
     b = getBase()
     h = getHeig()
     a = araT(b,h)
     print("Your area is: " + str(a))
                
#pre: requires area and perimeter values
#post: calculates displays area and perimeter for rectangles
def rectCalc():
     l = getLeng()
     w = getWidt()
     a = ara(l,w)
     p = perim(l,w)
     print("Your area is: " + str(a))
     print("Your perimeter is: " + str(p))
def polyCalc():
    sn = getSideNums()
    l =  getLeng()
    r = getRad()
    a = araP(sn,l,r)
    p = perimP(sn,l)
    print("Your area is: " + str(a))
    print("Your perimeter is: " + str(p))
#pre: client program
#during: have a mental breakdown
#post: displays area and perimeter
def main():
    print("The following program calculates the area and perimeter of geometrical shape")
    print("Which of the following shapes are you working with ? 1) - Triangle 2) - Polygon 3) - Rectangle")
    shape = input()
    if shape == "1":
        triCalc()
    elif shape == "2":
        polyCalc()
    elif shape == "3":
        rectCalc()
    else:
        print("That wasn't an option")

main()
#this program is terriblie and awful and I wanna cry and i should paid attention in algebra/geometry :,(
