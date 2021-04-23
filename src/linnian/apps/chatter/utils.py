from .chat_types import *


def easy_key(content: str, group: int, globaled: bool = False) -> Key:
    '''免去实例化N个对象创建key'''
    
    return Key.create(
        content=content,
        scope=Scope.create(
            group=group,
            globaled=globaled
        )
    )


def easy_reply(changer: int, text: List[str] = None,
               image: Union[Path, str] = None) -> Reply:
    
    '''免去实例化N个对象创建reply'''
    
    return Reply.create(
        ReplyContent.create(
            text,image
        ),
        changer
    )

def easy_chat(key: Key, reply: Reply) -> Chat:
    '''配合easykey,easyreply,免去实例化N个对象创建chat'''
    
    return Chat.create(key=key, reply=reply)