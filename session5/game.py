import random
count = 0

while True:
    num1 = random.randint(1,30)
    num2 = random.randint(1,15)
    saiso = random.randint(-3,3)
    sum = num1 + num2 + saiso 
    print("{} + {} = {}".format(num1, num2, sum))
    ans = input("T or F?").lower()

    if saiso == 0:
        if ans == "t":
            print("Correct")
            count += 1
            print("Diem cua ban la {}".format(count))
        if ans == "f":
            print("Wrong")
            count -= 1
            print("Diem cua ban la {}".format(count))
    if saiso != 0:
        if ans == "t":
            print("Wrong")
            count -= 1
            print("Diem cua ban la {}".format(count))
        if ans == "f":
            print("Correct")
            count += 1
            print("Diem cua ban la {}". format(count))

