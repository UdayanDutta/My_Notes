def simple_interest(p, t, r):
    print('The principle amount is', p)
    print('The time period is', t)
    print('The rate of interest is', r)

    simple_interest = (p * t * r) / 100

    print('The Simple Interest is', simple_interest)

    return simple_interest

#driver code
simple_interest(1000,5,4)