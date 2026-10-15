# AI & ML Training

<img width="400" height="400" alt="qr" src="https://github.com/user-attachments/assets/9de87d9c-44bc-47db-b3f2-75a914313ec4" />

## Install 

Follow [Jupyter Lab](https://jupyter.org/install) guide and install

```bash
pip install jupyterlab

jupyter lab
```

Jupyter Notebook (simpler UI)

```bash
pip install notebook

jupyter notebook
```

## Install Installation (Advanced)

[UV Installation](https://docs.astral.sh/uv/getting-started/installation/) Guide

Start a [Jupyter Notebook with UV](https://docs.astral.sh/uv/guides/integration/jupyter/) Project

```bash
uv init project
cd project
uv add --dev ipykernel

# optional
uv add --dev uv 
```

## Run Jupyter Lab Server 

### (Web Browser Mode)

```bash
uv run --with jupyter jupyter lab
```

### VS Code

- VS Code docs on [jupyter-notebooks](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)
- [Jupyter Extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) for VS Code

### Zed Editor

Go to settings.json, and add this `feature_flag`.

```json
"feature_flags": {
    "tabular-data-preview": "on",
    "notebooks": "on",
},
```
