ages = []

number = int(input("how many age do you want to compare?"))

for n in range(number):
    ages.append(int(input("Enter age: ")))

ages.sort()

print(ages[0])

