#this program defines the a function which implements the sieve of Atkin
from math import sqrt,ceil

def primes(n):
    if n<2:
        return []
    l=n/2-1+n%2
    sieve=[True]*(l+1)
    for i in xrange(int(sqrt(n))>>1):
        if not sieve[i]:
            continue
        for j in xrange((i*(i+3)<<1)+3,l,(i<<1)+3):
            sieve[j]=False
    primes=[2]
    primes.extend([(i<<1)+3 for i in xrange(l) if sieve[i]])
    return primes
#Normal method for Primes
def primes2(n):
    primes=[2]
    flag=False
    for i in xrange(3,n):
        flag=False
        for j in xrange(2,i/2):
            if i%j==0:
                flag=True
                break
        if flag==False:
            primes.append(i)
    primes.remove(4)       
    return primes
def prime2(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False
    r=[]
    for (i, isprime) in enumerate(a):
        if isprime:
            r.append(i)
            for n in xrange(i*i, limit, i):     # Mark factors non-prime
                a[n] = False
    return r

#Return the list of all prime numbers using the Sieve of Atkin
def sieveOfAtkin(end):
    assert end > 0, "end must be >0"
    lng = ((end // 2) - 1 + end % 2)
    sieve = [False] * (lng + 1)

    x_max, x2, xd = int(sqrt((end-1)/4.0)), 0, 4
    for xd in xrange(4, 8*x_max + 2, 8):
        x2 += xd
        y_max = int(sqrt(end-x2))
        n, n_diff = x2 + y_max*y_max, (y_max << 1) - 1
        if not (n & 1):
            n -= n_diff
            n_diff -= 2
        for d in xrange((n_diff - 1) << 1, -1, -8):
            m = n % 12
            if m == 1 or m == 5:
                m = n >> 1
                sieve[m] = not sieve[m]
            n -= d

    x_max, x2, xd = int(sqrt((end-1) / 3.0)), 0, 3
    for xd in xrange(3, 6 * x_max + 2, 6):
        x2 += xd
        y_max = int(sqrt(end-x2))
        n, n_diff = x2 + y_max*y_max, (y_max << 1) - 1
        if not(n & 1):
            n -= n_diff
            n_diff -= 2
        for d in xrange((n_diff - 1) << 1, -1, -8):
            if n % 12 == 7:
                m = n >> 1
                sieve[m] = not sieve[m]
            n -= d

    x_max, y_min, x2, xd = int((2 + sqrt(4-8*(1-end)))/4), -1, 0, 3
    for x in xrange(1, x_max + 1):
        x2 += xd
        xd += 6
        if x2 >= end: y_min = (((int(ceil(sqrt(x2 - end))) - 1) << 1) - 2) << 1
        n, n_diff = ((x*x + x) << 1) - 1, (((x-1) << 1) - 2) << 1
        for d in xrange(n_diff, y_min, -8):
            if n % 12 == 11:
                m = n >> 1
                sieve[m] = not sieve[m]
            n += d

    primes = [2, 3]
    if end <= 3:
        return primes[:max(0,end-2)]

    for n in xrange(5 >> 1, (int(sqrt(end))+1) >> 1):
        if sieve[n]:
            primes.append((n << 1) + 1)
            aux = (n << 1) + 1
            aux *= aux
            for k in xrange(aux, end, 2 * aux):
                sieve[k >> 1] = False

    s  = int(sqrt(end)) + 1
    if s  % 2 == 0:
        s += 1
    primes.extend([i for i in xrange(s, end, 2) if sieve[i >> 1]])

    return primes




#Timing the 3 methods of calculating primes
if __name__=='__main__':
    from timeit import Timer
    t=Timer('primes(10000)','from __main__ import primes')
    t2=Timer('prime2(10000)','from __main__ import prime2')
    t3=Timer('sieveOfAtkin(10000)','from __main__ import sieveOfAtkin')
    print t.timeit(100),' ',t2.timeit(100),' ',t3.timeit(100)

    
    
