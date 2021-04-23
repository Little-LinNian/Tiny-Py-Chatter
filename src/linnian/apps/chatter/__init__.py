from pathlib import Path
import time
from .chat_types import Key, Reply, ReplyContent, Scope, Chat
import ujson
import aiofiles
from loguru import logger as log


class Chatter():

    def __init__(self, config_file: str, backup_path: str = False):
        '''成功兽人(x 人士,癫疯之作,十年脑栓,猝死警告(xxxxxx\n
        传入配置文件路径,和备份目录(可选)
        '''

        path = Path(config_file)
        path = Path(config_file.replace(path.name, ''))
        if not Path(config_file).is_file() and not path.is_dir():
            log.warning('配置文件不存在')
            log.warning('将在5s后新建配置文件')
            time.sleep(5)
            log.success('完成!')
            path.mkdir()

        self.configfile = config_file
        self.configfile_path = Path(self.configfile)
        if backup_path:
            self.backup_Path = Path(backup_path)
            if not self.backup_Path.is_dir():
                log.warning('备份目录不存在')
                log.warning('5s后将自动创建备份目录')
                time.sleep(5)
                self.backup_Path.mkdir()
                log.success('成功')

        else:
            self.backup_Path = False
        self.load_file()  # 确保实例化对象时被文件加载

    def helloworld(self):
        log.info('开始初始化文件')
        time.sleep(5)
        open(self.configfile, mode='w+').write('{"Hello": "World"}')
        log.success('初始化文件成功')

    async def aload_file(self):
        '''异步加载ChatLib文件,方便从文件热刷新
        注意: 这是一个不安全方法
        注意: 不save()就加载将会导致一些奇怪的问题
        '''

        try:
            f = await aiofiles.open(self.configfile, encoding='utf-8')
            f_dict = ujson.loads(await f.read())
            self.chatlib = f_dict
            log.success(f'ChatLib {self.configfile} 文件加载成功')
        except Exception as e:
            log.error(f'ChatLib {self.configfile} 文件出现问题')
            log.error(e)
            log.warning(f'因为 {e} 所以将在5s后重新初始化文件')
            self.helloworld()
            await self.aload_file()

    def load_file(self):
        '''加载ChatLib文件
        注意: 这是一个不安全方法
        注意: 不save()就加载将会导致一些奇怪的问题
        '''

        try:
            f = open(self.configfile, encoding='utf-8')
            f_dict = ujson.load(f)
            self.chatlib = f_dict
            log.success(f'ChatLib {self.configfile} 文件加载成功')
        except Exception as e:
            log.error(f'ChatLib {self.configfile} 文件出现问题')
            log.error(e)
            log.warning(f'因为 {e} 所以将在5s后重新初始化文件')
            self.helloworld()
            self.load_file()

    async def save(self):
        '''保存内存中的chatlib到配置文件中,这可是个好方法,记得多用hh'''

        if self.chatlib:
            if self.backup_Path:
                b = await aiofiles.open(f'{str(self.backup_Path)}/{str(self.configfile_path.name)}-{time.time()}-backup.json', mode='w+', encoding='utf-8')
                orgin = await aiofiles.open(self.configfile, encoding='utf-8')
                orgin_str = await orgin.read()
                await b.write(
                    orgin_str
                )
                log.success('备份成功')
            else:
                log.warning('未设定备份目录，但不影响')
            async with aiofiles.open(self.configfile, encoding='utf-8', mode='w+') as f:

                data = ujson.dumps(self.chatlib)
                await f.write(data)
                log.success('保存成功')
        else:
            log.error('chatlib为空，保存操作无效')

    async def set(self, chat: Chat):
        '''传入Chat实例,
        当Chat的key存在时将会更新其对应reply,
        不存在时新建Key: Reply,
        记得 await save()
        '''

        self.chatlib[chat.key.json()] = chat.reply.json()
        log.success('设置成功')

    async def get_reply(self, key: Key) -> Reply:
        '''获得key对应的reply
        存在返回Reply实例
        不存在返回None
        tips: None的bool值为False
        '''

        try:
            reply = Reply(**ujson.loads(self.chatlib[key.json()]))
            return reply
        except:
            return None

    async def remove(self, key: Key) -> bool:
        '''移除key对应的reply,移除成功返回True,否则返回False
        记得 await save()
        '''

        try:
            del self.chatlib[key.json()]
            log.success('移除成功')
            return True

        except:
            log.error('移除失败')
            return False
