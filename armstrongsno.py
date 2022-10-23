n = int(input("Enter three digit number : "))
sum = 0
temp = n
while temp > 0:
    digit = temp % 10
    sum += digit * digit * digit
    temp = temp//10
 
if sum==n:
    print('It is an Armstrong number')
else:
    print('It is not an Armstrong number')
 
