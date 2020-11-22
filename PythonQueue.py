# Initialize the queue
names = []

# For loop asking for 10 individual names and appends each to the names list
for i in range(0,10):
    acceptedName = str(input("Please enter a name: "))
    names.append(acceptedName)

# Second for loop that deques/pops and prints each name
for j in range(0, len(names)):
    print(names.pop(0))
