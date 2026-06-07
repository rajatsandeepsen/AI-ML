# AI & ML Training

![QR For this Repo](/qr.png)

## Install Installation

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
