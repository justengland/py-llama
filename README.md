# python on llama

## Code mostly copied from https://mer.vin/2024/07/llama-3-1-fine-tune
- **app.py:** This file builds models using Torch and Unslöth.
- **local.py:** Uses Unslöth to combine a base Llama model with fine tunings for local usage.
- **huggingface.py:** Combines a base Llama model with fine tunings and publishes models to Hugging Face.
- **Modelfile:** Used to create a model for generating Ollama consumable models.
- **Modelfile.remote:** Used for publishing Hugging Face images into Ollama.


### Create model

```bash
conda create -y --name py_model python=3.10
conda activate py_model
conda install -y pytorch==2.2.0 cudatoolkit torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia
pip install xformers==0.0.24
pip install bitsandbytes
pip install "unsloth[conda] @ git+https://github.com/unslothai/unsloth.git"

# Create the model
./app.py
```

### Run model locally
Create the ollama m
```bash
ollama create -f Modelfile llama-py
ollama run llama-py
```

### Push Code to Huggingface and Ollama
```bash
./
ollama create -f Modelfile.remote justengland/llama-py
ollama push justengland/llama-py
```

### Troubleshooting
pytorch can be tricky I made the mistake of installing the dependencies to the root python system rather than the 
conda environment. Also, the deps seem to change frequently. Keep uptodate by monitoring this thread for the latest 
configuration.
see https://github.com/unslothai/unsloth/issues/73 for dep updates


RuntimeError: Unsloth: The file 'llama.cpp/llama-quantize' or 'llama.cpp/quantize' does not exist.
https://github.com/unslothai/unsloth/issues/748
```bash
cd llama.cpp
git checkout b3345
git submodule update --init --recursive
make clean
make all -j
git log -1
```


