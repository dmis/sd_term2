from aiohttp import web
from time import sleep


async def hello(request):
    try:
        sleep(1)
    finally:
        return web.Response(body='{\'type\': \'aiohttp\'}')


app = web.Application()
app.add_routes([web.get('/', hello)])
web.run_app(app, port=8888)
