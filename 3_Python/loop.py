
print("Please provide a number to calculate the factorial: ", end="")
number = int(input())

result = 1
for i in range(2,(number+1)):
    result *= i
print(result)

result = 1
i = 2
while(i<=number):
    result *= i
    i+=1
print(result)
