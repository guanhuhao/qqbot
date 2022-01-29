# -*- coding: UTF-8 -*-
from nonebot.command import CommandSession
from nonebot.plugin import on_command

from nonebot.natural_language import NLPSession, IntentCommand
from nonebot.experimental.plugin import on_command, on_natural_language

from services.saying.saying import RandomGetSaying

import pymongo 

__plugin_name__ = '说一句二次元经典语录'
__plugin_usage__ = (
    '用法：\n'
    '对我说：经典语录\n'
)

saying_permission = lambda sender: (not sender.is_privatechat) or sender.is_superuser

@on_command('famous saying in anime', permission=saying_permission)
async def _(session: CommandSession):
    result = RandomGetSaying()
    await session.send(result)

@on_natural_language(keywords={'经典语录'}, permission=saying_permission)
async def _(session: NLPSession):
    # 置信度为 90，意为将此会话当作 'weather' 命令处理
    return IntentCommand(90, 'famous saying in anime')