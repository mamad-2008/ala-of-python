print("Prime Checker")
num = int(input("Enter number: "))
i = 2
flag = 0
total = 0
while i < num:
if num % i == 0:      # ❌ Error: No indentation after while loop
flag = 1              # ❌ Should be indented inside if
print("Divisible by", i)   # ❌ Should be indented inside if
total = total + i     # ❌ Should be indented inside if
i = i + 1             # ❌ Should be inside while loop

if flag == 0:
print("Prime Number")     # ❌ Missing indentation
else:
print("Not Prime"         # ❌ Missing closing bracket )

print("Sum of checked numbers:", total)

if total > num:
print("Sum bigger")       # ❌ Missing indentation
else:
print("Sum smaller")      # ❌ Missing indentation