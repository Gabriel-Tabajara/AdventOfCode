file = open('Day1Input.txt')
sum = 0
higherSum = 0
for i in file.readlines():
    if i != '\n': 
        sum += int(i)
        if sum > higherSum: 
            higherSum = sum
    else: sum = 0

print(higherSum)


