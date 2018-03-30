def is_prime(num):
    try:
        num=int(num)
    except ValueError, TypeError:
        return False
    if num <=0: return False
    return 0 not in [num % i for i in range(1 if num < 2 else 2, int(num**.5)+1)]
