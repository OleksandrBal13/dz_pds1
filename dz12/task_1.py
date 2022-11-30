import concurrent.futures
import time

def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)

num1 = 111
num2 = 222
num3 = 333
num4 = 444
num5 = 555

start = time.time()
factorial(num1)
factorial(num2)
factorial(num3)
factorial(num4)
factorial(num5)
end = time.time() - start

if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as thread_executor:
        start_thread = time.time()
        number_1 = thread_executor.submit(factorial, num1).result()
        number_2 = thread_executor.submit(factorial, num2).result()
        number_3 = thread_executor.submit(factorial, num3).result()
        number_4 = thread_executor.submit(factorial, num4).result()
        number_5 = thread_executor.submit(factorial, num5).result()
        end_thread = time.time() - start_thread

    with concurrent.futures.ProcessPoolExecutor(max_workers=2) as process_executor:
        start_process = time.time()
        number_1 = process_executor.submit(factorial, num1).result()
        number_2 = process_executor.submit(factorial, num2).result()
        number_3 = process_executor.submit(factorial, num3).result()
        number_4 = process_executor.submit(factorial, num4).result()
        number_5 = process_executor.submit(factorial, num5).result()
        end_process = time.time() - start_process

    end_dict = {'no_pool_executor': end,'thread': end_thread,'process': end_process}
    print(f'And the winner is {min(end_dict, key=end_dict.get)} method with {end_dict[min(end_dict, key=end_dict.get)]} time result')