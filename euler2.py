
from itertools import groupby
number=28
trainglen=7



def sieve(limit):
    not_prime = []
    prime = []
    for i in xrange(2, limit + 1):
        if i not in not_prime:
            prime.append(i)
            for j in xrange(i * i, limit + 1, i):

                not_prime.append(j)
    return prime

def factors(number):
    fact = []
    count = 1
    limit=int(number**.5)+1
    lists=sieve(limit)
    print(lists)
    i=0
    f=[]

    while True:
        if number%lists[i]==0:
            number=number/lists[i]
            fact.append(lists[i])
        else:
            i=i+1

        if number==1:
            break;
    print(fact)
    f=[len(list(group)) for key, group in groupby(fact)]
    for xx in range(0,len(f)):
        count=count*(f[xx]+1)
    print(count)
    return count



while True:
    trainglen=trainglen+1
    number=number+trainglen
    print(number)
    factor=factors(number)
    print(factor)
    if factor>500:
        break;
print(number)

<<<<<<< HEAD
=======
def sleep_decorator(function):

    """
    Limits how fast the function is
    called.
    """

    def wrapper(*args, **kwargs):
        sleep(2)
        return function(*args, **kwargs)
    return wrapper


@sleep_decorator
def print_number(num):
    return num


for num in range(1, 6):
    print(print_number(num))





