import time

def measure_latency(fn,*a,**k):
    s=time.perf_counter(); r=fn(*a,**k); return r,time.perf_counter()-s

def latency_decorator(fn):
    def w(*a,**k): return measure_latency(fn,*a,**k)
    return w
