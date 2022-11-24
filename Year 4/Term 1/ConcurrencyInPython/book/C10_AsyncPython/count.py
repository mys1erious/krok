import time
import asyncio


async def count_down(name, delay):
    indents = (ord(name) - ord('A')) * '\t'

    n = 3
    while n:
        await asyncio.sleep(delay)
        duration = time.perf_counter() - start
        print('-'*40)
        print(f'{duration} \t{indents}{name} = {n}')
        n-=1


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [
        loop.create_task(count_down('A', 1)),
        loop.create_task(count_down('B', 0.8)),
        loop.create_task(count_down('C', 0.5))
    ]

    start = time.perf_counter()
    loop.run_until_complete(asyncio.wait(tasks))

    print('-'*40)
    print('Done')
