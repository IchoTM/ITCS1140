def getLeng():
    length = float(input("Give me a length: "))
    return length
def getWidt():
    width = float(input("Give me a width: "))
    return width
def ara(l,w):
    area = l * w
    return area
def perim(l,w):
    perimeter = 2 * (l + w)
    return perimeter
def dispResult(a,p):
    print("Your area is: " + str(a))
    print("Your perimeter is: " + str(p))

def main():

    l = getLeng()
    w = getWidt()
    a = ara(l,w)
    p = perim(l,w)
    dispResult(a,p)

main()
