import asyncio
import os.path
import aiohttp
import aiofiles
from timeit import default_timer as timer


async def get_html(session, url):
    async with session.get(url, ssl=False) as res:
        return await res.text()


async def download_html(session, url):
    async with session.get(url, ssl=False) as res:
        filename = f'output/{os.path.basename(url)}.html'

        async with aiofiles.open(filename, 'wb') as f:
            while True:
                chunk = await res.content.read(1024)
                if not chunk:
                    break
                await f.write(chunk)

        return await res.release()


async def main(url):
    async with aiohttp.ClientSession() as session:
        await download_html(session, url)


if __name__ == '__main__':
    urls = [
        'http://packtpub.com',
        'http://python.org',
        'http://docs.python.org/3/library/asyncio',
        'http://aiohttp.readthedocs.io',
        'http://google.com'
    ]

    start = timer()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(
        *(main(url) for url in urls)
    ))
    print(f'Took {timer() - start}')
