# python on llama

## Prereqs

### Setup Unsloth

```bash
conda create -y --name py_model python=3.10
conda activate py_model
conda install -y pytorch==2.2.0 cudatoolkit torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia
pip install xformers==0.0.24
pip install bitsandbytes
pip install "unsloth[conda] @ git+https://github.com/unslothai/unsloth.git"

# Create the model
python app.py

# Build for ollama
ollama create -f Modelfile llama3.1-python

# Run locally
ollama run llama3.1-python
```

### Troubleshooting
pytorch can be tricky I made the mistake of installing the the depencies to the root python system rather than the 
conda environment. Also the deps seem to change frequently, so
see https://github.com/unslothai/unsloth/issues/73 for dep updates
