import multiprocessing
import time

def factorize(*numbers):
    results = []
    
    for n in numbers:
        factors = []
        for i in range(1, n + 1):
            if n % i == 0:
                factors.append(i)
        results.append(factors)      
    return tuple(results)

def parallel_factorize(numbers):
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        results = pool.map(factorize, numbers)
    return results

if __name__ == '__main__':
    
    start_time = time.time()
    a, b, c, d = factorize(128, 255, 99999, 10651060)
    end_time = time.time()
    execution_time = end_time - start_time
    print(a, b, c, d)
    print(f"Час за виконання функції без паралельного обчислення: {execution_time}")
    
    start_time_1 = time.time()
    a, b, c, d = parallel_factorize([128, 255, 99999, 10651060])
    end_time_1 = time.time()
    execution_time_1 = end_time_1 - start_time_1
    print(f"Час за виконання функції з паралельним обчисленням: {execution_time_1}")
    print(a, b, c, d)
    
    
    # assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    # assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    # assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    # assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
