Student = {"Name" : "John" ,
           "Credits" : 10 ,
           "Scholorship" : True ,
           "Focus" : "Computer Science/Game Design"}

print(Student)

currentStat = Student["Credits"]

print(currentStat)

if currentStat < 50:
    print("Must be second year")
else:
    print("idk man")

if Student["Name"] == "John":
    print("Man what are you doing here")

if Student["Scholorship"] == False:
    print("Dang, prolly still don't cost too much tho right?")
else:
    print("Niceeee. free ride")

if Student["Major"] == "Computer Science/Game Design":
    print("HA nerd")

#I have zero clue how college credit works and this function is a prime example of that#
#However teehee i have an excuse kinda? cause I'm a dual enrolment student so the whole credit system is the least of my concern rn#
def credScav(s):
    if s["Credits"] <= 10:
        print("You new here or something?")
        gr = "F"
        return gr
    elif s["Credits"] <= 20:
        print("I suppose thats good???")
        gr = "D"
        return gr
    elif s["Credits"] <= 30:
        print("goooood??? i thinkkkk??? I don't knowwww???")
        gr = "A"
        return gr
    else:
        print("I give up IDK how creds work")
        gr = "??????"
        return gr

def main(s):
    gr = credScav(s)
    print(gr)
    
main(Student)
