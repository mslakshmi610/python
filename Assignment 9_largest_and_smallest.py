first = [ ]
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number '))
    first.append(numbers)
print("Maximum element in the list is :", max(first), "\nMinimum element in the list is :", min(first))