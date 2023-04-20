def prime(number):
    for i in range(2, number):
        if number%i == 0:
             return False
        else:
             continue
    return True

def print_primes(number):
    for i in range(2, number):
        if prime(i):
            print(i)

def one_function(number):
    for i in range(number):
        for j in range(2, i):
            if i % j == 0:
                break
            else:
                continue
        print(i)