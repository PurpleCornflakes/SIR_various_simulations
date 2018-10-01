import time

def timeit(method):
    def timed(*args, **keywords):
        ts = time.time()
        result = method(*args, **keywords)
        te = time.time()
        print('%r  %2.2f ms' % (method.__name__, (te - ts) * 1000))
        return result
    return timed