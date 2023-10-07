import time
import multiprocessing


def get_divisors(number: int) -> list[int]:
    """Get all divisors of a number.

    Args:
        number (int): The number to find divisors for.

    Returns:
        List[int]: The list of divisors.
    """

    divisors = []
    for i in range(1, number+1):
        if number % i == 0:
            divisors.append(i)
    return divisors


def factorize_sync(*numbers: int) -> list[list[int]]:
    """Factorize numbers synchronously.

    Args:
        *numbers (int): Numbers to factorize

    Returns:
        List[List[int]]: List of list of divisors for each number.
    """

    factors = []
    for number in numbers:
        divisors = get_divisors(number)
        factors.append(divisors)
    return factors


def factorize_parallel(*numbers: int) -> list[list[int]]:
    """Factorize numbers in parallel.

    Args:
        *numbers (int): Numbers to factorize

    Returns:
        List[List[int]]: List of list of divisors for each number.
    """

    num_processes = multiprocessing.cpu_count()
    with multiprocessing.Pool(processes=num_processes) as pool:
        results = pool.map(get_divisors, numbers)
    return results


if __name__ == "__main__":

    start_time = time.time()
    a, b, c, d = factorize_sync(128, 255, 99999, 10651060)
    end_time = time.time()
    print(f"Synchronous execution time: {end_time - start_time} seconds")

    start_time = time.time()
    a, b, c, d = factorize_parallel(128, 255, 99999, 10651060)
    end_time = time.time()
    print(f"Parallel execution time on {multiprocessing.cpu_count()} cores: {end_time - start_time} seconds")

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]

    print("Ok")