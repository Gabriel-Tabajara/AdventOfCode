file = open('Day1Input.txt')
sum = 0
higherSum = 0
secondHigherSum = 0
thirdHigherSum = 0
for i in file.readlines():
    if i != '\n': 
        sum += int(i)
        if sum >= thirdHigherSum and sum < secondHigherSum: 
            thirdHigherSum = sum
        elif sum >= secondHigherSum and sum < higherSum: 
            thirdHigherSum = secondHigherSum
            secondHigherSum = sum
        elif sum >= higherSum:
            thirdHigherSum = secondHigherSum
            secondHigherSum = higherSum
            higherSum = sum
        
    else: sum = 0

print(higherSum + secondHigherSum + thirdHigherSum)


