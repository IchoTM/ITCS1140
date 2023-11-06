class houseType(object):

    def __init__(self, s, ba, be, c):

        self.style = s
        self.numofBath = ba
        self.numofBed = be
        self.cost = c

    def __str__(self):

        rep = "\nStyle : " + str(self.style) + "\nNum of Baths : " + str(self.numofBath) + "\nNum of Beds : " + str(self.numofBed) + "\nCost : " + str(self.cost)
        return rep



def main():

    myHouse = houseType("Ranch", 3.5, 4, 300000)
    print(myHouse)

main()
