def power_check(n, b):
    if n == 1:
        return True
    if n < b or n % b != 0:
        return False
    return power_check(n // b, b)