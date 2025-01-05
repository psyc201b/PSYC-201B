# Option 1: Configuring your own computer

This option is ideal if you prefer working on your own computer. It requires a bit more setup, but is a great option if you want to customize your workflow and/or learn about reproducible computing configurations.

## macOS/linux

### Git Setup
1. Install the [Homebrew package manager](https://brew.sh/) (macOS only)
2. Install the latest version of `git` by running `brew install git` (macOS only)
3. Install the github CLI by running `brew install gh` (macOS only)
4. Connect your local git to your github account by [following these instructions](https://docs.github.com/en/get-started/getting-started-with-git/set-up-git)

### Python Setup
1. Following the [Miniconda Terminal setup instructions](https://docs.anaconda.com/miniconda/install/)
2. Verify the installation by running `which python` in your terminal and looking for a 'miniconda' in the outputted path
3. Create a new conda environment for the class by running `conda create --name 201b -c ejolly -c conda-forge -c defaults pymer4`
4. Activate the enviroment by running `conda activate 201b`
5. Verify the installation by running `which python` in your terminal and looking for a 'envs/201b' in the outputted path

#### If using [VSCode](https://code.visualstudio.com/)
- Install the additional packages after activating the environment: `pip install ipykernel ruff`
- Open up VSCode and install the following extensions: [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python), [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter), [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance), [Ruff](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff)
- Try creating a new Python notebook and choosing `201b` as the kernel

#### If using [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/index.html)
- Install the additional packages after activating the environment: `conda install -c conda-forge jupyterlab`
- Launch JupyterLab by running `jupyter lab` in your terminal
- Try creating a new Python notebook and choosing `201b` as the kernel

