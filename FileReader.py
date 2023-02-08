# Raihan Khalil Abdillah, 30065695
# AT2.4 Question 1
# File Reader

file = open("vehicles.txt", 'r')
count = 0
for car in file:
    print(car, end="")
    # count += 1
    # print("Line Count:", count)
    # print()

file.close()
