#!/usr/bin/env python3
from unsloth import FastLanguageModel
import os

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name='lora_model',
    max_seq_length=2048,
    dtype=None,
    load_in_4bit=True,
)
FastLanguageModel.for_inference(model)

# model.save_pretrained_gguf("gguf_output", tokenizer, quantization_method="q4_k_m")
# Used locally
model.save_pretrained_gguf("gguf_output", tokenizer, quantization_method="q8_0")
# model.save_pretrained_gguf("gguf_output", tokenizer, quantization_method="f16")

# this pushes to hugging face
# model.push_to_hub_gguf(
#     "justengland/Llama-3.1-8B-bnb-4bit-python",
#     tokenizer,
#     quantization_method=["q4_k_m", "q8_0", "q5_k_m", ],
#     token=os.getenv("HF_TOKEN"),
# )
