# ruff: noqa: E402

from nonebot import get_plugin_config, require
from nonebot.plugin import PluginMetadata, inherit_supported_adapters

require("nonebot_plugin_alconna")
require("nonebot_plugin_uninfo")

from . import handler as handler
from .config import Config

__version__ = "1.0.3.post2"
__plugin_meta__ = PluginMetadata(
    name="奶龙魔法",
    description="世界就是一个巨大的奶龙~",
    usage="发送变奶龙+[图片]就会把目标变成奶龙",
    type="application",
    homepage="https://github.com/Refound-445/nonebot-plugin-nailongmagic",
    config=Config,
    supported_adapters=inherit_supported_adapters(
        "nonebot_plugin_alconna",
        "nonebot_plugin_uninfo",
    ),
)
config = get_plugin_config(Config)
