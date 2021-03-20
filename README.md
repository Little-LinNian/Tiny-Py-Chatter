# Tiny-Py-Chatter  
# Powerd By Redis Python3 Pydantic  
# 快速开始 pip install linnian-apps-chatter 
    from linnian.apps.chatter import Chater
    from linnian.apps.chatter.tool import Tool
    import asyncio
    # Tool为工具封装，可不实例化


    async def main():
        chat = Chater()  # 实例化一个Chatter对象，默认为localhost和6379
        await chat.set(
            Tool.createKey('qwq', 1234),  # 使用工具快速实例化Key
            Tool.createReply('qwq', 1234)  # 使用工具快速实例化Reply
        )
        print(
            await chat.get_reply(
                Tool.createKey('qwq', 1234))
        )

    asyncio.run(main())
  