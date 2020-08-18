# Assignment - Pro - 1 (Is it a Prime Number?)

isPrime = int(input("Please enter a number: "))

if isPrime > 1:
    for i in range(2,isPrime):
       if (isPrime % i) == 0:
           print(isPrime,"is not a prime number")
           break
    else:
        print(isPrime,"is a prime number")
    
else:
   print(isPrime,"is not a prime number")