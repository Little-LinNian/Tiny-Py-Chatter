from pathlib import Path
from linnian.apps.chatter import Chatter
from linnian.apps.chatter.utils import easy_chat, easy_key, easy_reply
from linnian.apps.chatter.chat_types import Chat
import asyncio

loop = asyncio.get_event_loop()

chatter = Chatter('test.json','./test-backup') # 务必在函数外实例化
example_key = easy_key('qwq',1234)
example_reply = easy_reply(1234,['qwq',1234],image=Path('./test.png'))
example_chat = easy_chat(example_key, example_reply)


async def main():
    await chatter.set(example_chat)
    reply = await chatter.get_reply(example_key)
    print(reply.content.image.absolute().as_uri()) # Out: 文件的绝对路径
    reply = await chatter.get_reply(example_key)
    print(reply.content.text) # Out: ['qwq', '1234']
    await chatter.save() 
    # test.json: {"Hello":"World","{\"content\": \"qwq\", \"scope\": {\"globaled\": false, \"group\": 1234}}":"{\"content\": {\"text\": [\"qwq\", \"1234\"], \"image\": \"test.png\"}, \"changer\": 1234}"}
    await chatter.remove(example_key)
    reply = await chatter.get_reply(example_key)
    print(reply) # Out: None

loop.run_until_complete(main())
