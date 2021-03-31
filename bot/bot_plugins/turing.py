# -*- coding: UTF-8 -*-
from nonebot.experimental.plugin import on_command, on_natural_language
from nonebot.natural_language import NLPSession, IntentCommand
from nonebot.command import CommandSession
import services.turing.chatbot as bot

#权限控制
turing_permission = lambda sender: (not sender.is_privatechat) or sender.is_superuser 

@on_command('聊天', permission=turing_permission)
async def _(session: CommandSession):
    if not session.state.get("sentence") :
        sentence = session.current_arg_text.strip()
    else :
        sentence = session.state.get("sentence")

    try:
        result = bot.ask(sentence)
    except ServiceException as e:
        result = e.message   

    await session.send(str(result))

@on_natural_language(keywords=None, permission=turing_permission)
async def _(session: NLPSession):
    # 使用 jieba 将消息句子分词
    print(session.msg_text.strip())
    arg = {}
    arg['sentence'] = session.msg_text.strip()
    # 置信度为 90，意为将此会话当作 'weather' 命令处理
    return IntentCommand(80, '聊天', args=arg)