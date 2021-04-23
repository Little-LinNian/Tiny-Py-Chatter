from pathlib import Path
from typing import Any, Union, List
from pydantic import BaseModel


class Scope(BaseModel):
    '''承载Key的作用域'''

    globaled: bool = False
    group: int

    def __init__(__pydantic_self__, **data: Any) -> None:
        super().__init__(**data)
        if __pydantic_self__.globaled:
            __pydantic_self__.group = 'Globaled'

    @classmethod
    def create(cls, group: int, globaled: bool = False) -> 'Scope':
        '''承载Key的作用域'''

        return cls(globaled=globaled, group=group)


'''
class Code(BaseModel):

    content: str

    @classmethod
    def create(cls,content: str) -> 'Code':
        return cls(content=content)

class CQ(Code):
    pass

class Mirai(Code):
    pass

class Plain(BaseModel):

    content: List[str]

    @classmethod
    def create(cls,content: List[str]) -> 'Plain':
        return cls(content=content)

class Image(BaseModel):

    uri: Union[Path,HttpUrl]
    
    @classmethod
    def create(cls,
    uri: Union[Path,HttpUrl]) -> 'Image':
        return cls(uri=uri)
'''


class ReplyContent(BaseModel):

    text: List[str] = None
    image: Union[Path, str] = None

    @classmethod
    def create(cls,
               text: List[str] = None,
               image: Union[Path, str] = None
               ) -> "ReplyContent":
        '''承载Reply的Content'''

        return cls(
            text=text,
            image=image
        )


class Key(BaseModel):

    content: str
    scope: Scope

    @classmethod
    def create(cls, content: str, scope: Scope) -> 'Key':
        '''承载键值'''

        return cls(content=content, scope=scope)


class Reply(BaseModel):

    content: ReplyContent
    changer: int

    @classmethod
    def create(cls, content: ReplyContent,  changer: int) -> 'Reply':
        return cls(content=content, changer=changer)


class Chat(BaseModel):

    key: Key
    reply: Reply

    @classmethod
    def create(cls, key: Key, reply: Reply) -> 'Chat':
        return cls(key=key, reply=reply)
