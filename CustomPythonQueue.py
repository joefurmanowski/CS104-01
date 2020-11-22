# Initialize the queue
names = []

# Ask user how many names are in the queue
numberOfNames = int(input("How many people are in the queue?: "))

# For loop asking for numberOfNames individual names and appends each to the names list
for i in range(0, numberOfNames):
    acceptedName = str(input("Please enter name {}/{}: ".format(i+1, numberOfNames)))
    names.append(acceptedName)

# Second for loop that deques/pops each name and prints each
for j in range(0, len(names)):
    print(names.pop(0))
