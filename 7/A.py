import time
import random

def time_decorator(decorated_func):
    def helper(*xs, **kws):
        t0 = time.time()
        print('Start time:', t0)
        decorated_func(*xs)
        t1 = time.time()
        print('End time:', t1)
        print('Execution time:', str(t1 - t0))
    return helper

def counter_decorator(decorated_func):
    def helper(*xs, **kws):
        helper.calls += 1
        print('Function calls count:', helper.calls)
        return decorated_func(*xs, **kws)
    helper.calls = 0
    return helper

def method_decorator(decorated_method):
    def helper(**kws):
        print(kws)
        def count(arg, x, y, z):
            coefs = [3, 7, 15, 18]
            return x * coefs[0] - y * coefs[1] + z * coefs[2] + coefs[3]
        print(xs, kws)
        return decorated_method(xs[0], count(*xs))
    return helper
