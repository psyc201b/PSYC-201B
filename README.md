# 201b

Source code for stat 201b.


## Dev notes

### One-time environment setup
- `conda create -n 201b python=3.11 pip ruff ipykernel jupyter-book -c conda-forge`
- `conda activate 201b`
- `conda install pymer4 -c ejolly -c conda-forge -c defaults`
- `pip install -r requirements.txt`
- `jupyter-book build .`
- `jupyter-book config sphinx .`

### Using environment
- `conda activate 201b`
- `sphinx-autobuild . _build/html -b html`
- Open `http://127.0.0.1:8000/` in browser

When editing jupyter-book config files rerun this command before sphinx-autobuild:  
`jupyter-book build . && jupyter-book config sphinx .`
