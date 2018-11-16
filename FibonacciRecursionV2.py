"""FibonacciRecursionV1"""
def _fib(num):
    """ Calculate fibonacci """
    if num == 0:
        return (0, 1)
    else:
        num_a, num_b = _fib(num // 2)
        num_c = num_a * (num_b * 2 - num_a)
        num_d = num_a * num_a + num_b * num_b
        if num % 2 == 0:
            return (num_c, num_d)
        else:
            return (num_d, num_c + num_d)
print(_fib(int(input()))[0])

