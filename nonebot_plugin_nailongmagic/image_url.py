from typing import (
    AsyncIterator,
    Tuple,
    Union,
)
from nonebot import logger
from nonebot.matcher import current_bot, current_event, current_matcher
from nonebot_plugin_alconna.uniseg import Image, Segment, UniMessage, At, Reply
from nonebot_plugin_alconna.uniseg.tools import image_fetch
from nonebot_plugin_uninfo import get_interface
from PIL import Image as PILImage
from PIL.ImageFile import ImageFile as PILImageFile
from io import BytesIO


async def extract_source(seg: Union[Segment, Image, At, Reply], solve_at: bool = False) -> Union[PILImageFile, Reply]:
    if type(seg) is Image:
        pass
    elif type(seg) is Reply:
        return seg
    elif type(seg) is At and solve_at:
        interface = get_interface(current_bot.get())
        user = await interface.get_user(seg.target)
        url = user.avatar
        seg = Image(url=url)
    else:
        raise NotImplementedError
    image = await image_fetch(
        current_event.get(),
        current_bot.get(),
        current_matcher.get().state,
        seg,
    )
    if not image:
        raise RuntimeError("Cannot fetch image")
    return PILImage.open(BytesIO(image))


async def iter_sources_in_message(
        message: UniMessage,
        solve_at: bool = False,
) -> AsyncIterator[Tuple[Union[PILImageFile, Reply], Segment]]:
    for seg in message:
        try:
            yield await extract_source(seg, solve_at=solve_at), seg
        except NotImplementedError:
            continue
        except Exception as e:
            logger.warning(f"Failed to process {seg!r}: {type(e).__name__}: {e}")
            logger.opt(exception=e).debug("Stacktrace")
