import asyncio
import aiohttp
from config import Config
import time
import random

config = Config()
print(config()['requests'][0]['method'])


async def execute(req, session):
    body = req['body'] if req['body'] != 'None' else None
    return await session.request(req['method'], req['url'], headers=req['headers'], data=body)


async def request(req):
    req_txt = req['url']
    # Application should perform load testing stage by stage. There shouldn't be a stop between stages
    for stage in config.stages:
        print(f'New stage for {req_txt}')
        for rep in range(int(stage['repeats'])):
            req_num = 0
            success = 0
            errors = 0
            start = time.time()
            duration = stage['duration']
            t_end = start + duration

            rps_from = stage['rps_from']
            rps_to = stage['rps_to']
            if rps_from > rps_to:
                rps_from = stage['rps_to']
                rps_to = stage['rps_from']
            while time.time() < t_end:

                # Rate can differ from second to second.
                count_rate = random.randint(rps_from, rps_to)
                # During every stage application should send requests to given URLs asynchronously with given rate
                req_num += count_rate
                async with aiohttp.ClientSession(loop=loop) as session:
                    futures = [execute(req, session) for _ in range(count_rate)]
                    responses = await asyncio.gather(*futures)
                    for r in responses:
                        if 200 <= r.status <= 299:
                            success += 1
                        else:
                            errors += 1
                    # print(responses)
                if (t_end - time.time()) > 0:
                    delay = random.randint(0, (t_end - time.time()) // 2)
                    duration -= delay
                    await asyncio.sleep(delay)
        # After every repetition of every stage, application should print report:

        print(
            f' {req_num} of requests to {req_txt}, {success / req_num * 100}% of success requests (200-299 status code), {errors / req_num * 100}% of errors (other status codes), '
            f' average query duration is {duration / req_num} seconds.')
        await asyncio.sleep(stage['timeout'])


async def tasks():
    start = time.time()
    tasks = []
    for i in config.requests:
        tasks.append(asyncio.ensure_future(request(i)))

    await asyncio.wait(tasks)
    print("Process took: {:.2f} seconds".format(time.time() - start))


loop = asyncio.get_event_loop()
result = loop.run_until_complete(tasks())
loop.close()
