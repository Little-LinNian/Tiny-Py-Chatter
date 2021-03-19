import aioredis
import asyncio
import ujson


class Chat():
    def __init__(self, addr: str = 'localhost', port: int = 6379) -> None:
        self.addr = addr
        self.port = port

    async def add(self, key: str, group: int, member: int, reply: str, mirai_code: bool = False):
        conn = await aioredis.create_connection((self.addr, self.port))
        keyw = ujson.dumps({'key': key, 'group': group})
        replyw = ujson.dumps(
            {'reply': reply, 'member': member, 'mirai_code': mirai_code})
        await conn.execute('SET', keyw, replyw)

    async def get_reply(self, key: str, group: int):
        '''当有结果时返回结果，没有则返回None   OwO'''
        conn = await aioredis.create_connection((self.addr, self.port))
        keyw = ujson.dumps({'key': key, 'group': group})
        resp = await conn.execute('get', keyw)
        if resp is None:
            return 
        else:
            replyw = ujson.loads(resp)
            reply = replyw['reply']
            return reply
    async def remove(self, key: str,group: int):
        conn = await aioredis.create_connection((self.addr, self.port))
        keyw = ujson.dumps({'key': key, 'group': group})
        resp = await conn.execute('del',keyw)
        if resp == 0:
            raise KeyError("没有相应键")
        return resp

'''
async def main():
    # await Chat().add('qwq',1234,1234,'owo')
    #print(await Chat().get_reply('ppp', 1234))
    print(await Chat().remove('ppp',1234))
asyncio.run(main())
'''