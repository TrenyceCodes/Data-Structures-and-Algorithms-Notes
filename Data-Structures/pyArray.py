# collection = single "varaible" used to store multiple variables

# List = [] ordered and changeable, Duplicates are allowed in this
# Set = {} unordered and immutable, but adding and removing is allowed and duplicates aren't
# Tuple = () ordered and not changeable, but duplicates are allowed and this is a faster option

# examples
fruits = ["apple", "orange", "banana", "coconut"]
#print(fruits)
#print(fruits[::2]) #step to two elements in array
#[start:end:step]
#print(fruits[2:])
#print(fruits[:2])

#print(dir(fruits))

for x in fruits:
    print(x)

#examples of set
cars = {"tesla", "fort", "honda", "bus"}
cars.add("low-rider")
cars.pop() #removes a random item from string
cars.remove("tesla") #removes tesla from cars set
cars.clear() #clears out set
print(cars)

# examples of tuple
colors = ("red", "yellow", "blue", "blue")
print(colors.index("yellow"))
print(colors.count("yellow"))
