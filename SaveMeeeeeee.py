text_file = open("Aleph.txt", "r")
##print(text_file.read(1))
##print(text_file.read(4))
##
##x = 0
##while x < 3:
##    m = text_file.readline()
##
##    if "L" in m:
##        print("Found it")
##    x = x +1
##
##for line in text_file:
##    print(line)

txtFil = open("Fear.txt", "a")
txtFil.write("Line Uno\n")
txtFil.write("Es line Dos\n")
txtFil.write("Una line tres\n")
txtFil.close()

tf = open("Fear2.txt", "w")
lines = ["Line\n", "Woah another line\n", "Three whole lines!\n"]
tf.writelines(lines)
tf.close()
