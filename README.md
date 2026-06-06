#

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

### Zed Editor

Go to settings.json, and add this `feature_flag`.

```json
"feature_flags": {
    "tabular-data-preview": "on",
    "notebooks": "on",
},
```
