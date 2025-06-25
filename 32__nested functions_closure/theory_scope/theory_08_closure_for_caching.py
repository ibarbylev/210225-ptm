import time

def long_function(num):
    time.sleep(3)
    return list(range(num))

def memoize():
    cache = {}

    def get_or_compute(key, compute_function):
        if key not in cache:
            cache[key] = compute_function(key)
        return cache[key]


    return get_or_compute

cached_computation = memoize()

start = time.time()
print(cached_computation(10, long_function))  # Долгая операция
print("Время расчёта:", time.time() - start)

start = time.time()
print(cached_computation(10, long_function))  # Берёт из кеша (быстро)
print("Время получения из кэша:", time.time() - start)
