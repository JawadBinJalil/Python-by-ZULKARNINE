with open("text.txt", mode="r") as file:
    for line in file.readlines():
        words= line.split(" ")
        print(line, end="")



#readlines()-> for reading every line of a text file
#strip()-> for every word
