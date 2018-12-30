from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv

print("The script is called:", script)
print("Your firts variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", int(third))

mult = int(input("Multiplier of the third variable is:"))

print("{} is the value".format(mult*int(third)))
