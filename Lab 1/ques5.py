num = int(input("Enter a number: "))

def isPrime(num):
    flag = True
    for i in range(2,num):
        if num % i == 0:
            flag = False
    return flag

if isPrime(num):
    print(f"{num} is prime")
else:
    print(f"{num} is not prime")