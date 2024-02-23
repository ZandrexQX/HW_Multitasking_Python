import asyncio
import time
from pathlib import Path


async def count_words(file: Path, start_time):
    with open(file, encoding='utf-8') as f:
        text = f.read()
    print(f"In file {file.name}: {len(text.split())} words. Time - {time.time() - start_time:.4f}\n")


async def task(path: Path):
    start_time = time.time()
    files = [file for file in path.iterdir() if file.is_file()]

    for file in files:
        await count_words(file, start_time)



if __name__ == '__main__':
    asyncio.run(task(Path.cwd()))