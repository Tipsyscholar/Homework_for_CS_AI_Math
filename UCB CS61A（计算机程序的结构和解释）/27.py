import asyncio
import time

import asyncio
import aiohttp
import time

async def fetch_midterm(semester, year, midterm):
    filename = f"61a-{semester}{year}-{midterm}.pdf"
    url = f"https://cs61a.org/exam/{semester}{year}/{midterm}/{filename}"
    print(f"Fetching {semester}{year}: {url}")
    start = time.time()
    try:
        session = aiohttp.ClientSession()
        # Tell servers and proxies not to use cached content
        headers = {
            "Cache-Control": "no-cache",
            "Pragma": "no-cache",
        }

        response = await session.get(url, headers=headers)
        if response.status == 200:
            pdf_bytes = await response.read()

            f = open(f"midterms/{filename}", "wb")
            f.write(pdf_bytes)
            f.close()

            print(f' {time.time() - start} seconds to fetch {semester}{year} ({len(pdf_bytes)} bytes)')
        else:
            print(f' {time.time() - start} seconds to get status {response.status} for {semester}{year}')

        await response.release()
        await session.close()

    except aiohttp.ClientError as e:
        print(f"Error fetching {url}: {e}")

async def fetch_midterms():
    start = time.time()

    #coros = []
    for year in [19, 20, 21, 22, 23, 24, 25]:
        for semester in ["sp", "su", "fa"]:
            midterms = []
            if semester == "su":
                midterms = ["midterm"]
            else:
                midterms = ["mt1", "mt2"]
            for midterm in midterms:
                # Why isn't this running concurrently?
                await fetch_midterm(semester, year, midterm)
                #coros.append(fetch_midterm(semester, year, midterm))
    #await asyncio.gather(*coros)

    print(f'{time.time() - start} seconds to fetch all midterms')

asyncio.run(fetch_midterms())

# Example where students are all waiting for various things.

async def cupcake():
    await asyncio.sleep(2)
    return 12

async def doordash_boba():
    await asyncio.sleep(1)
    cupcakes_in_classroom["vanilla"] = 2
    await asyncio.sleep(9)

cupcakes_in_classroom = {"carrot cake": 10, "chocolate": 2}

async def apollo():
    print("Starting Apollo!")
    await asyncio.sleep(600)

async def kay():
    print("Starting Kay!")
    await doordash_boba()

async def harry():
    if "vanilla" not in cupcakes_in_classroom:
        print("Starting Harry!")
        cupcakes = await cupcake()
        # cupcakes_in_classroom may be different!
        # cupcakes_in_classroom["vanilla"] = 2
        if "vanilla" in cupcakes_in_classroom:
            cupcakes_in_classroom["vanilla"] = cupcakes_in_classroom["vanilla"] + cupcakes
        else:
            cupcakes_in_classroom["vanilla"] = cupcakes

async def start():
    await asyncio.gather(
        apollo(),
        kay(),
        harry(),
    )

asyncio.run(start())

# Timer examples, where students predict how long each will take.

async def sleep1():
    start = time.time()
    await asyncio.sleep(2)
    await asyncio.sleep(2)
    await asyncio.sleep(2)
    print(f'sleep1 took {time.time() - start} seconds')

asyncio.run(sleep1())

async def sleep2():
    start = time.time()
    await asyncio.gather(asyncio.sleep(2),
                         asyncio.sleep(2),
                         asyncio.sleep(2))
    print(f'sleep2 took {time.time() - start} seconds')

asyncio.run(sleep2())

async def blocking_sleep(seconds):
    time.sleep(seconds)

async def sleep3():
    start = time.time()
    await asyncio.gather(blocking_sleep(2),
                         blocking_sleep(2),
                         blocking_sleep(2))
    print(f'sleep3 took {time.time() - start} seconds')

asyncio.run(sleep3())

async def new_blocking_sleep(seconds):
    await asyncio.to_thread(lambda: time.sleep(seconds))

async def sleep4():
    start = time.time()
    await asyncio.gather(new_blocking_sleep(2),
                         new_blocking_sleep(2),
                         new_blocking_sleep(2))
    print(f'sleep4 took {time.time() - start} seconds')

asyncio.run(sleep4())