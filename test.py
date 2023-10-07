import multiprocessing

def factorize_single(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def factorize(*numbers):
    num_processes = 4  # Встановлюємо кількість процесів на 4
    with multiprocessing.Pool(processes=num_processes) as pool:
        results = pool.map(factorize_single, numbers)
    return results

if __name__ == "__main__":
    import time

    # # Синхронна версія
    # start_time = time.time()
    # a, b, c, d = factorize(128, 255, 99999, 10651060)
    # print("Синхронна версія зайняла %s секунд" % (time.time() - start_time))

    # Паралельна версія
    start_time = time.time()
    a, b, c, d = factorize(128, 255, 99999, 10651060)
    print("Паралельна версія зайняла %s секунд" % (time.time() - start_time))