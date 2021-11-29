n = int(input("Enter the Number:"))
sum = 0
for i in range(1, n):
    if(n % i == 0):
        sum = sum + i
if(sum == n):
    print("The Entered Number Is a Perfect Number")
else:
    print("The Entered Number Is Not a Perfect Number")


