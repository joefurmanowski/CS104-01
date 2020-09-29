numberOfTests = 0
score = 0
total = 0
average = 0.0
scoreCount = 0

numberOfTests = int(input("Please enter the number of tests you want to average: "))

#Make these next 3 lines repeat until scoreCount = numberOfTests
#for loop
score = int(input("Please enter a score: "))
scoreCount = scoreCount + 1
total += score


average = total/scoreCount
print("The average is ",average)
