import aioredis
import ujson
from .tool import Key, Reply, Tool



class Chater():
    '''简单封装 qwq'''

    def __init__(self, addr: str = 'localhost', port: int = 6379) -> None:
        self.addr = addr
        self.port = port

    async def connect(self):
        '''连接数据库并返回连接对象Owo'''
        conn = await aioredis.create_connection((self.addr, self.port))
        return conn

    async def set(self, key: Key, reply: Reply):
        '''需要一个Key实例和Reply实例\n
        可以从linnian.apps.chatter.tool引用\n
        Key Reply (原始)\n
        Tool(包含快速生成工具)
        '''
        conn = await self.connect()
        await conn.execute('SET', key.json(), reply.json())

    async def get_reply(self, key: Key) -> Reply:
        """
        当有结果时返回结果，没有则返回None   OwO\n
        需要一个Key实例\n
        可以从linnian.apps.chatter.tool引用\n
        Key(原始)\n
        Tool(包含快速生成工具)
        """
        conn = await self.connect()
        resp = await conn.execute('get', key.json())
        if resp is None:
            return
        else:
            replyw = ujson.loads(resp)
            return Reply(**replyw)

    async def remove(self, key: Key):
        """
        当有结果时返回结果，没有则返回None   OwO\n
        需要一个Key实例\n
        可以从linnian.apps.chatter.tool引用\n
        Key(原始)\n
        Tool(包含快速生成工具)
        """
        conn = await self.connect()
        resp = await conn.execute('del', key.json())
        if resp == 0:
            raise KeyError("没有相应键")
        return resp

'''
async def main():
    await Chater().set(Tool.createKey('qwq',1234),
    Reply(reply='qwq', member=1234))
    await Chater().get_reply(Tool.createKey('qwq',1234))
asyncio.run(main())
'''
