import math

# time(x) = O(sqrt(x))*

def is_prime(x):
    if x == 2:
        return True
    upper = math.ceil(math.sqrt(x)) + 1   #ceil - округляем вверх sqrt(x), функция библиотеки math*
    for i in range(2, upper):
        if x % i != 0:
            i += 1
        else:
            return False
    return True
    
def test1():
    for i in range(2, 50):
        if is_prime(i):
            print(i, end=" ")
    print()

def test2():
    primes = []
    x = 2
    cnt = 0
    while cnt != 50:
        if is_prime(x):
            print(x, end=" ")
            cnt += 1
            primes.append(x)
        x += 1
    print()
    print(len(primes))

def nth_prime(n):
    x = 2
    cnt = 0
    while cnt != n:
        if is_prime(x):
            # print(x, end=" ")
            cnt += 1
        x += 1
    return x - 1

#y = is_prime(input())
#z = test1(input())
#h = test2(input())
x = nth_prime(int(input()))
#print(y, z, h, x)
print(x)

#[in1]: 1241241

#[out1]: 1241241 - isn't a prime

#[in2]: 104743
#[out2]:104743 - is a prime numb



