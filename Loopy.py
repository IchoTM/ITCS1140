##x = 0
##y = 3
##if x <= 2 and y == 4:
##    print("Of course its less than 2 can you not count???")
##elif y == 3:
##    print("Idek anymore I feel bad for being ahead lmao")
##else:
##    print("Yeah thats more than 2")
##
##while x < 2:
##    print("X = " + str(x))
##    x = x + 1
##
##teststr = "ITCS-1140"
##
##for x in teststr:
##    print(str(x))
##
##lions = "Detroit lions are garbage"
##
##for x in lions:
##    print(str(x))
##print(len(lions))
##if len(lions) == 25:
##    print("hey look 4 lions make 100")
##    print(str(lions) * 4)
##    print(len(str(lions) * 4))

def wordCheck():
    rule = str
    chekvic = str
    cot = int
    cot = 0

    rule = str(input("What are we checking for? : "))
    chekvic = str(input("What are we checking? : "))
    
    for r in rule:
        print(r)
        for c in chekvic:
            print(c)
            if r == c:
                print("is in : " + r)
            else:
                print("its not in there")
            cot = cot + 1
    print("this code ran " + str(cot) + " times!")

def start():
    
    print("this program compares two strings aginst eachother letter by letter")

def update():

    while True:
        wordCheck()

start()
update()
