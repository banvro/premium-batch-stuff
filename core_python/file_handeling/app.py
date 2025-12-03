
# file handeling

# open()

# modes

# w ---> creating a new file

# file = open("myfirstfile.txt", "x")
# file.close()

# how to write in text file 

# mode ---> w 

# xyz = open("myfirstfile.txt", "w")
# xyz.write("This is my data...!")
# xyz.close()


# x = open("abcxyz.txt", "w")
# x.write("heyyyyyyyyyyyyyyy!")
# x.close()

# zx = open("abcxyz.txt", "a")
# zx.write("\n this is new data added by append mode.")
# zx.close()


file = open("myfirstfile.txt", "r")
# print(file.read())
# print(file.readline())
# print(file.readline())

print(file.readlines())
file.close()