import multiprocessing
import time
from pathlib import Path


def count_words(file: Path, start_time):
    with open(file, encoding='utf-8') as f:
        text = f.read()
    print(f"In file {file.name}: {len(text.split())} words. Time - {time.time() - start_time:.4f}\n")


def task(path: Path):
    start_time = time.time()
    files = [file for file in path.iterdir() if file.is_file()]
    processes = []

    for file in files:
        process = multiprocessing.Process(target=count_words, args=(file, start_time))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()


if __name__ == '__main__':
    task(Path.cwd())