from nonebot_plugin_alconna.uniseg import Image
from nonebot_plugin_uninfo import User,UniSession
from io import BytesIO
import torch

from diffusers import AutoPipelineForImage2Image
from PIL import Image as PILImage

from ..config import config

# import os
# os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

token = config.nailongmagic_hf_token
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


pipeline = AutoPipelineForImage2Image.from_pretrained(
    "stable-diffusion-v1-5/stable-diffusion-v1-5", torch_dtype=torch.float16 if torch.cuda.is_available() else None, variant="fp16", use_safetensors=True,
    cache_dir=config.nailongmagic_cache_dir,token=token
).to(device)


pipeline.load_lora_weights("refoundd/NailongT", weight_name="pytorch_lora_weights.safetensors", adapter_name="nailong",
                           cache_dir=config.nailongmagic_cache_dir,token=token)

if torch.cuda.is_available():
    pipeline.enable_model_cpu_offload()


# remove following line if xFormers is not installed or you have PyTorch 2.0 or higher installed
# pipeline.enable_xformers_memory_efficient_attention()
# prepare image


async def check(init_image:PILImage, prompt: str) -> Image:
    init_image = init_image.convert("RGB")
    generator = torch.Generator(device=device).manual_seed(33)
    # pass prompt and image to pipeline
    negative_prompt = "bad architecture, unstable, poor details, blurry"

    lora_scale = 1
    image = pipeline(
        prompt=prompt, image=init_image, negative_prompt=negative_prompt, num_inference_steps=30,
        cross_attention_kwargs={"scale": lora_scale},
        guidance_scale=12.5, strength=0.8, generator=generator, width=512, height=512
    ).images[0]
    # image = init_image
    imageIO = BytesIO()
    image.save(imageIO, format='JPEG', )
    imageIO.getvalue()
    return Image(raw=imageIO)
