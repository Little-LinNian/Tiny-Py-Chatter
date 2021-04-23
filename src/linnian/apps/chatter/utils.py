from .chat_types import *


def easy_key(content: str, group: int, globaled: bool = False) -> Key:
    return Key.create(
        content=content,
        scope=Scope.create(
            group=group,
            globaled=globaled
        )
    )


def easy_reply(changer: int, text: List[str],
               image: Union[Path, str] = None) -> Reply:
    return Reply.create(
        ReplyContent.create(
            text,image
        ),
        changer
    )
