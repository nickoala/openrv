import utime, gc

def time(f):
    def g(*args, **kwargs):
        start = utime.ticks_us()
        result = f(*args, **kwargs)
        end = utime.ticks_us()
        print('us taken: {}'.format(end - start))
        return result
    return g

def memory(f):
    def g(*args, **kwargs):
        start = gc.mem_alloc()
        result = f(*args, **kwargs)
        end = gc.mem_alloc()
        print('bytes used: {}'.format(end - start))
        return result
    return g
