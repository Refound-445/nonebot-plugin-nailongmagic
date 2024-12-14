from nonebot_plugin_alconna.uniseg import Image
from io import BytesIO
import torch

from diffusers import AutoPipelineForImage2Image
from PIL import Image as PILImage

from ..config import config
# import os
# os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
from nonebot import require

require("nonebot_plugin_localstore")

import nonebot_plugin_localstore as store

token = config.nailongmagic_hf_token
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
cache_dir = store.get_plugin_cache_dir() / "data/nailongmagic"

pipeline = AutoPipelineForImage2Image.from_pretrained(
    "stable-diffusion-v1-5/stable-diffusion-v1-5", torch_dtype=torch.float16 if torch.cuda.is_available() else None, variant="fp16", use_safetensors=True,
    cache_dir=cache_dir,token=token
).to(device)


pipeline.load_lora_weights("refoundd/NailongT", weight_name="pytorch_lora_weights.safetensors", adapter_name="nailong",
                           cache_dir=cache_dir,token=token)

if torch.cuda.is_available():
    pipeline.enable_model_cpu_offload()


# remove following line if xFormers is not installed or you have PyTorch 2.0 or higher installed
# pipeline.enable_xformers_memory_efficient_attention()
# prepare image


async def check(init_image:PILImage, prompt: str) -> Image:
    init_image = init_image.convert("RGB")
    generator = torch.Generator(device=device).manual_seed(33)
    # pass prompt and image to pipeline

    lora_scale = 1
    image = pipeline(
        prompt, image=init_image, num_inference_steps=30, cross_attention_kwargs={"scale": lora_scale},
        generator=generator
    ).images[0]

    imageIO = BytesIO()
    image.save(imageIO, format='JPEG', )
    imageIO.getvalue()
    return Image(raw=imageIO)
