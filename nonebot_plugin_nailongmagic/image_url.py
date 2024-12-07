from typing import (
    AsyncIterator,
    Tuple,
    Union,
)
from nonebot import logger
from nonebot.matcher import current_bot, current_event, current_matcher
from nonebot_plugin_alconna.uniseg import Image, Segment, UniMessage
from nonebot_plugin_alconna.uniseg.tools import image_fetch
from PIL import Image as PILImage
from io import BytesIO


async def extract_source(seg: Union[Segment, Image]) -> PILImage:
    if type(seg) is not Image:
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
) -> AsyncIterator[Tuple[PILImage, Segment]]:
    for seg in message:
        try:
            yield await extract_source(seg), seg
        except NotImplementedError:
            continue
        except Exception as e:
            logger.warning(f"Failed to process {seg!r}: {type(e).__name__}: {e}")
            logger.opt(exception=e).debug("Stacktrace")
