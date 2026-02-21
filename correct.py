print("Prime Checker")
num = int(input("Enter number: "))

i = 2
flag = 0
total = 0

while i < num:
    if num % i == 0:
        flag = 1
        print("Divisible by", i)
        total = total + i
    i = i + 1

if flag == 0:
    print("Prime Number")
else:
    print("Not Prime")

print("Sum of checked numbers:", total)

if total > num:
    print("Sum bigger")
else:
    print("Sum smaller")