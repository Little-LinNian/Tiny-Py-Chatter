from pydantic import BaseModel


class Key(BaseModel):
    key: str
    group: int


class Reply(BaseModel):
    reply: str
    member: int
    mirai_code: bool = False


class Tool():
    '''提供一些便捷工具Owo'''
    def createKey(key: str, group: int) -> Key:
        '''快速生成Key实例'''
        return Key(key=key,group=group)

    def createReply(reply: str, member: int, mirai_code: bool = False) -> Reply:
        '''快速生成Reply实例'''
        return Reply(reply=reply, member=member, mirai_code=mirai_code)
