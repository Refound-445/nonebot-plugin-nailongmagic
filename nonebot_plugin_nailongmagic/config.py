from pathlib import Path
from typing import Any, List, Optional

from cookit.pyd import field_validator
from nonebot import get_plugin_config
from pydantic import BaseModel, Field

class Config(BaseModel):
    proxy: Optional[str] = None

    nailongmagic_need_superuser: bool = True
    nailongmagic_list_scenes: List[str] = Field(default_factory=list)
    nailongmagic_blacklist: bool = True
    nailongmagic_user_blacklist: List[str] = Field(default_factory=list)
    nailongmagic_priority: int = 100

    nailongmagic_tip: List[str] = ["奶龙已生成~{$checked_result}"]
    nailongmagic_prompt: List[str] = ["nailong"]

    nailongmagic_cache_dir: Path = Field(
        default_factory=lambda: Path.cwd() / "data" / "nailongmagic",
    )
    nailongmagic_auto_update_model: bool = True

    nailongmagic_hf_token: Optional[str] = None


    @field_validator(
        "nailongmagic_tip",
        mode="before",
    )
    def transform_to_list(cls, v: Any):  # noqa: N805
        return v if isinstance(v, list) else [v]

config = get_plugin_config(Config)
