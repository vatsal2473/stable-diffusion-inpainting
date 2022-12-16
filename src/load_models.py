from diffusers import StableDiffusionInpaintPipeline
import torch

def load_stable_diffusion_inpainting_model():
    pipe = None
    device = "cuda"
    model_path = "runwayml/stable-diffusion-inpainting"

    pipe = StableDiffusionInpaintPipeline.from_pretrained(
        model_path,
        revision="fp16", 
        torch_dtype=torch.float16,
        use_auth_token=True
    ).to(device)

    return pipe