import aioredis
import ujson
from .tool import Key, Reply, Tool


class Redis:
    _redis = None
        
    def __init__(self, addr: str, port: int ) -> None:
        self.addr = addr
        self.port = port

    async def get_redis_pool(self):
        if not self._redis:
            self._redis = await aioredis.create_redis_pool((self.addr,self.port))
            return self._redis
                                            
    async def close(self):
        if self._redis:
            self._redis.close()
            await self._redis.wait_closed()


class Chater():
    '''简单封装 qwq'''

    def __init__(self, addr: str = 'localhost', port: int = 6379) -> None:
        self.addr = addr
        self.port = port
        self.redis = Redis(addr, port)

    async def set(self, key: Key, reply: Reply):
        '''需要一个Key实例和Reply实例\n
        可以从linnian.apps.chatter.tool引用\n
        Key Reply (原始)\n
        Tool(包含快速生成工具)
        '''
        pool = await self.redis.get_redis_pool()
        await pool.set(key.json(), reply.json())
        await self.redis.close()

    async def get_reply(self, key: Key) -> Reply:
        """
        当有结果时返回Reply实例\n
        没有则返回None   OwO\n
        需要一个Key实例\n
        可以从linnian.apps.chatter.tool引用\n
        Key(原始)\n
        Tool(包含快速生成工具)
        """
        pool = await self.redis.get_redis_pool()
        resp = await pool.get(key.json())
        if resp is None:
            return
        else:
            replyw = ujson.loads(resp)
            return Reply(**replyw)
        await self.redis.close()
    
    async def remove(self, key: Key):
         """
         当有结果时返回结果，没有则返回0   OwO\n
         需要一个Key实例\n
         可以从linnian.apps.chatter.tool引用\n
         Key(原始)\n
         Tool(包含快速生成工具)
         """
         pool = await self.redis.get_redis_pool()
         resp = await pool.delete(key.json())
         if resp == 0:
             raise KeyError("没有相应键")
         return resp
         await self.redis.close()
        

'''
async def main():
    await Chater().set(Tool.createKey('qwq',1234),
    Reply(reply='qwq', member=1234))
    await Chater().get_reply(Tool.createKey('qwq',1234))
asyncio.run(main())
'''
