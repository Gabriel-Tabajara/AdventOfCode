file = open('Day2Input.txt')
mySum = 0
for line in file.readlines():
    letters = line.split(" ")
    print(letters)
    if letters[1] == "Z" or letters[1] == "Z\n":
        if letters[0] ==  "A":
            mySum += 3
        elif letters[0] == "B":
            mySum += 9
        else:
            mySum += 6
    elif letters[1] == "Y" or letters[1] == "Y\n":
        if letters[0] ==  "A":
            mySum += 8
        elif letters[0] == "B":
            mySum += 5
        else:
            mySum += 2
    else:
        if letters[0] ==  "A":
            mySum += 4
        elif letters[0] == "B":
            mySum += 1
        else:
            mySum += 7

print(mySum)