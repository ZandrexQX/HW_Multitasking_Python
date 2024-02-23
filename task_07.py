import asyncio
import random
import threading
import multiprocessing
import time

arr = [random.randint(1, 100) for i in range(0, 1000000)]

def sum_arr(arr: list):
    sums = []
    for i in range(1, 11):
        begin = int(len(arr) / 10 * (i - 1))
        end = int(len(arr) / 10 * i)
        sum_for = sum(arr[i] for i in range(begin, end))
        sums.append(sum_for)
    return sum(sums)

def sum_part(arr: list, sums: list, i: int, start_time: time):
    begin = int(len(arr) / 10 * (i - 1))
    end = int(len(arr) / 10 * i)
    sum_for = sum(arr[i] for i in range(begin, end))
    sums.append(sum_for)
    print(f"Sum_{i} = {sum_for} Time - {time.time() - start_time:.4f}")

async def sum_part_async(arr: list, sums: list, i: int, start_time: time):
    begin = int(len(arr) / 10 * (i - 1))
    end = int(len(arr) / 10 * i)
    sum_for = sum(arr[i] for i in range(begin, end))
    sums.append(sum_for)
    print(f"Sum_{i} = {sum_for} Time - {time.time() - start_time:.4f}")

# res = sum_arr(arr)
res_test = sum(arr)
# print(f"{res == res_test}")

def sum_thread():
    threads = []
    sums_thread = []

    for i in range(1, 11):
        start_time = time.time()
        t = threading.Thread(target=sum_part, args=(arr, sums_thread, i, start_time))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    return sum(sums_thread)

def sum_multiprocessing():
    global arr
    with multiprocessing.Manager() as manager:
        sums_process = manager.list()
        processes = []
        for i in range(1, 11):
            start_time = time.time()
            t = multiprocessing.Process(target=sum_part, args=(arr, sums_process, i, start_time))
            processes.append(t)
            t.start()

        for p in processes:
            p.join()
        return sum(list(sums_process))

async def sum_async():
    global arr
    sums_async = []
    start_time = time.time()
    for i in range(1, 11):
        await sum_part_async(arr, sums_async, i, start_time)

    return sum(sums_async)

if __name__ == '__main__':
    print("Threading\n-------------------------------------------")
    start_time_01 = time.time()
    res_01 = sum_thread()
    t_01 = time.time() - start_time_01
    print(f"Sum in threading = {res_01} Time threading: {t_01:.4f}")
    print(f"Sum threading is_true: {res_01 == res_test}")
    print("-------------------------------------------")

    print("Multiprocessing\n-------------------------------------------")
    start_time_02 = time.time()
    res_02 = sum_multiprocessing()
    t_02 = time.time() - start_time_02
    print(f"Sum in multiprocessing = {res_02} Time multiprocessing: {t_02:.4f}")
    print(f"Sum multiprocessing is_true: {res_02 == res_test}")
    print("-------------------------------------------")

    print("Async\n-------------------------------------------")
    start_time_03 = time.time()
    res_03 = asyncio.run(sum_async())
    t_03 = time.time() - start_time_03
    print(f"Sum in async = {res_03} Time async: {t_03:.4f}")
    print(f"Sum async is_true: {res_03 == res_test}")
    print("-------------------------------------------")

    print(f"Result:\n"
          f" - Threading_time: {t_01:.4f}\n"
          f" - Multiprocess_time: {t_02:.4f}\n"
          f" - Async_time: {t_03:.4f}")
