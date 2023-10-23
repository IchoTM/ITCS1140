# This code is absolute garbage do not use it as a ref #
# Please someone else upload a better code of this example #


##try:
##    num = float(input("Enter a number: "))
##except:
##    print("*extremly loud incorrect buzzer* try again dip stick")
sum1 = float

try:
    num1 = int(input("Ight we dividing. Gimme a number: "))
except(TypeError):
    print("*extremly loud incorrect buzzer* Try a number next time genius")


try:
    num2 = int(input("And another!: "))
except(TypeError):
    print("*extremly loud incorrect buzzer* Try a number next time genius")

try:
    sum1 = num1/num2
except(ZeroDivisionError):
    print("*extremly loud incorrect buzzer* Can't divide by zero stupid")
    
if sum1 >= 0:
    print(str(sum1))
