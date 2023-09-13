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
    length = float(input("Give me a length: "))
    return length
#pre: 
#post: returns width value
def getWidt():
    width = float(input("Give me a width: "))
    return width
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
#pre: client program
#post: displays area and perimeter
def main():
    print("The following program calculates the area and perimeter of geometrical shape")
    print("Which of the following shapes are you working with ? 1) - Triangle 2) - Circle 3) - Rectangle")
    shape = input()
    if shape == "1":
        triCalc()
    elif shape == "2":
        circCalc()
    elif shape == "3":
        rectCalc()
    else:
        print("That wasn't an option")

main()
