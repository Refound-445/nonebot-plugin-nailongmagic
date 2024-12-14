import os
from pathlib import Path
from typing import Any, List, Optional

from nonebot import get_plugin_config
from pydantic import BaseModel, Field
from nonebot import require

require("nonebot_plugin_localstore")

import nonebot_plugin_localstore as store

class Config(BaseModel):
    proxy: Optional[str] = None

    nailongmagic_need_superuser: bool = True
    nailongmagic_list_scenes: List[str] = Field(default_factory=list)
    nailongmagic_blacklist: bool = True
    nailongmagic_user_blacklist: List[str] = Field(default_factory=list)
    nailongmagic_priority: int = 100

    nailongmagic_tip: List[str] = ["奶龙已生成~{$checked_result}"]
    nailongmagic_prompt: List[str] = ["nailong"]

    nailongmagic_cache_dir: Path = store.get_plugin_cache_dir("data\nailongmagic")
    nailongmagic_auto_update_model: bool = True

    nailongmagic_hf_token: Optional[str] = None



config = get_plugin_config(Config)
