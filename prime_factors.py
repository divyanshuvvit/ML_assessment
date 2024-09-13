def prime_factors(n):
    factors = []

    count = 0
    while n % 2 == 0:
        n //= 2
        count +=1
    if count > 0:
        factors.append((2, count))

    factor = 3
    while factor * factor <= n:
        count = 0
        while n % factor == 0:
            n //= factor
            count += 1
        if count > 0:
            factors.append((factor, count))
        factor += 2
    if n > 2:
        factors.append((n, 1))

    return factors    