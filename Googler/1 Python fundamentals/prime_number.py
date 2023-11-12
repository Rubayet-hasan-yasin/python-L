import math


user_num = int(input("limit for prime: "))


def is_prime(num):
    for i in range(2, int(math.sqrt(num)+1)):
        if(num % i==0):
            return False
    return num>1

def findPrime(limit):
    prime = list()
    for i in range(2, limit+1):
        if(is_prime(i)):
            prime.append(i)
            # print(f"{i} is prime")
    return prime

        
        

print(findPrime(user_num))