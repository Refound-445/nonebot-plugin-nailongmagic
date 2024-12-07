import random
import re
from typing import Iterable,TypeVar

from nonebot import logger, on_message
from nonebot.adapters import Bot as BaseBot, Event as BaseEvent
from nonebot.permission import SUPERUSER
from nonebot.rule import Rule
from nonebot_plugin_alconna.uniseg import UniMessage, UniMsg,Text
from nonebot_plugin_uninfo import QryItrface, Uninfo

from .config import config
from .image_url import iter_sources_in_message
from .model import check

T = TypeVar("T")


def judge_list(lst: Iterable[T], val: T, blacklist: bool) -> bool:
    return (val not in lst) if blacklist else (val in lst)

async def nailong_rule(
        bot: BaseBot,
        event: BaseEvent,
        session: Uninfo,
        ss_interface: QryItrface,
        msg: UniMsg,
) -> bool:
    return (
        # check if it's a group chat
            bool(session.member)  # this prop only exists in group chats
            # user blacklist
            and (session.user.id not in config.nailongmagic_user_blacklist)
            # scene blacklist or whitelist
            and judge_list(
        config.nailongmagic_list_scenes,
        session.scene_path,
        config.nailongmagic_blacklist,
    )
            # if need superuser
            and ((not config.nailongmagic_need_superuser) or (await SUPERUSER(bot, event)))
    )


nailong = on_message(rule=Rule(nailong_rule), priority=config.nailongmagic_priority)


@nailong.handle()
async def handle_function(bot: BaseBot, ev: BaseEvent, msg: UniMsg, session: Uninfo):
    prompt=None
    for seg in msg:
        if type(seg) is Text and "变奶龙" in seg.text:
            prompt = re.search(r"变奶龙(\S+)", seg.text.replace(" ", ""))
            prompt = prompt.group(1) if prompt is not None else config.nailongmagic_prompt[random.randint(0, len(config.nailongmagic_prompt) - 1)]
            break
    if prompt is not None:
        async for source, seg in iter_sources_in_message(msg):
            try:
                check_res = await check(source,prompt)
            except Exception:
                logger.exception(f"Failed to check {seg!r}")
                continue
            template_str_all = config.nailongmagic_tip
            template_str = template_str_all[
                random.randint(0, len(template_str_all) - 1)
            ]
            mapping = {
                "$event": ev,
                "$target": msg.get_target(),
                "$message_id": msg.get_message_id(),
                "$msg": msg,
                "$ss": session,
                "$checked_result": check_res,
            }
            await UniMessage.template(template_str).format_map(mapping).finish()
