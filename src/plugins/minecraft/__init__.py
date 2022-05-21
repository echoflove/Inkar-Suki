from nonebot import on_command
from nonebot.adapters import Message
from nonebot.params import CommandArg
from nonebot.adapters.onebot.v11 import MessageSegment as ms
from .mcv import *

mcbv = on_command("mcbv",priority=5)
@mcbv.handle()
async def _():
    msg = await mcbedrockv()
    await mcbv.finish(msg)

mcjv = on_command("mcjv",priority=5)
@mcjv.handle()
async def _():
    msg = await mcjavav()
    await mcjv.finish(msg)