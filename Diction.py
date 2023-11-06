dic = {"404" : "Clueless" ,
       "Uninstalled" : "Fired"}
if "Dancing Balonga" in dic:
    print("I know what that is?")
else:
    print("Are you insane?")

dic["Link Rot"] = "When a webpage becomes obsolete"

print(dic)

dic["Dancing Balonga"] = "I don't even know man"

if "Dancing Balonga" in dic:
    print("I know what that is?")
else:
    print("Are you insane?")

del dic["Dancing Balonga"]

print(dic)
