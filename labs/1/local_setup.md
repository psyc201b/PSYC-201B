# 1. Configuring your computer for class

The follow instructions guide you through setting up your personal computer (macOS/linux or Windows) for class. This process might be a bit frustrating at first, but it's important to get right and you only have to do it once!

```{note}
If you're unable to get your computer configured by the end of Lab 1, or the end of this week (Jan 10th), please contact your instructors on Slack and we'll either help you trouble shoot or provide an alternative setup option.
```

## 1. Initial setup

First make sure you already have an existing [GitHub account](https://github.com/). Then after logging in you'll want to **create a [passkey](https://docs.github.com/en/authentication/authenticating-with-a-passkey/managing-your-passkeys#adding-a-passkey-to-your-account) for your account.** This will allow you to login into your account from your computer's terminal without entering a password.

Next we'll want to make sure that `git` is installed and setup on your computer. Pick the instructions based on your computer's operating system and open up a Terminal (macOS) or Command Prompt/PowerShell (windows):

````{tab-set}
```{tab-item} macOS
- Install the [Homebrew package manager](https://brew.sh/) or check if you have it installed `which brew`
- Install the latest version of `git` by running `brew install git`
- Install the [github CLI](https://github.com/cli/cli#installation) by running `brew install gh`
```

```{tab-item} windows
- Check if you have `git` installed by running `git --version`
- If not, install it using the [instructions here](https://git-scm.com/downloads/win)
- Install the [github CLI](https://github.com/cli/cli#installation) by running `winget install --id github.cli`
```
````

Finally we'll want to configure [git with your github account](https://docs.github.com/en/get-started/getting-started-with-git/set-up-git). Make sure your **username matches your Github userid** and your **email matches the [email you used on Github](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-email-preferences/setting-your-commit-email-address?platform=mac#setting-your-commit-email-address-on-github)**:
- Configure your git username by running `git config --global user.name "your-name"`
- Configure your git email by running `git config --global user.email "your-email"`
- Authenticate to github by running `gh auth login` and entering **the passkey you generated earlier**

🥳: Now you should be able to push/pull from your github account using the command line!

## 2. Python setup

Next we'll setup Python on your computer. While most computers come with Python installed, it's important that we don't "mess with" your computer's default Python installation. Instead, we'll use a popular Python package manager called [Miniconda](https://docs.anaconda.com/miniconda/install) which will allow us to create, manage, and install packages into **isolated** Python environments. This is important for a few reasons:

1. You can have multiple Python environments on your computer, each with their own set of packages and dependencies, e.g. if you're working on different projects with different needs.
2. It allows you and others to more easily perform **[reproducible research](https://rse.shef.ac.uk/conda-environments-for-effective-and-reproducible-research/04-sharing-environments/index.html)**

First follow the [Miniconda setup instructions here](https://docs.anaconda.com/miniconda/install/) for your computer's OS. Make sure to follow the directions for either the **macOS terminal** OR **windows command prompt/powershell**, not the graphical installer/website! You can then verify the installation by running `conda env list` your terminal. You should notice a "base" environment listed, which is the default Python environment that comes with your installation.

Next we're going to create a new Python environment for the class:  

```bash
conda create --name 201b -c ejolly -c conda-forge -c defaults pymer4
```

If that command doesn't work (windows 😠?) try this instead: 

```bash
conda create --name 201b -c conda-forge -c defaults python=3.11 pandas numpy seaborn matplotlib patsy joblib scipy scikit-learn
```

Next activate the environment by running `conda activate 201b`. You should see `(201b)` appear in your terminal prompt. You should also be able to verify that the `python` command is now pointing to the new environment by running `which python` (macOS) or `where python` (windows) in your terminal.

🥳: If you see a path that includes `201b` you're all set! 

```{tip}
Conda can be a little confusing to get used to at first and we won't spend too much time on it in class. But we've linked to some additioanl resources including a command references in the [cheatsheets](/pages/cheatsheets) section!
```

## 3. Coding environment setup

You should choose between 2 recommended options for your coding setup. Below we'll discuss the pros and cons of each and how to get started with them:

### Jupyterlab

[Jupyterlab](https://jupyterlab.readthedocs.io/en/stable/getting_started/overview.html) is an interactive data-analysis environment similar to Rstudio. It's a bit more beginner friendly and comes with useful configurations and extensions that make it easier to work with data in Python. 

To install it, make sure you've activated your class environment and run `conda install -c conda-forge jupyterlab`. Once complete, you can launch Jupyterlab by running `jupyter lab` in your terminal. This will always open a new tab in your web-browser with the working directory set to wherever you ran the command from.

From [the interface](https://jupyterlab.readthedocs.io/en/stable/user/interface.html) you can: browse files, create/edit `.py` files (Python scripts), create/edit `.ipynb` files (Jupyter notebooks), and more! Just remember, whenever you create/edit a notebook to work interactively, make sure to select the `201b` kernel from the dropdown menu in the upper right corner of the interface. This will ensure your code is run in the correct environment with the correct packages installed!

### Visual Studio Code

[VSCode](https://code.visualstudio.com/) is a popular, general-purpose IDE (integrated-development-environment) that runs as a standalone application on your computer. It's a bit more advanced than Jupyterlab, but it's also more powerful and customizable. It's the preferred way that Eshin likes to work with Python as well as other langauges (e.g. Javascript, bash, R, etc). It also has free access to [Github Copilot](https://github.com/features/copilot), a GenAI tool built right into VSCode, as well as tight integration with Github (e.g. changes, commits, push/pulls, etc).

To install VSCode, we'll first install a package in the class environmen that will make it "visible" to VSCode. After activating your class environment run `pip install ipykernel`. Then visit the [VSCode download page](https://code.visualstudio.com/download) and follow the instructions for your computer's OS. Once installed, you can open the app like you would any other app on your computer. 

Optionally, you can launch VSCode by running `code` in your terminal. To do so, open VSCode and open the Command Palette by running `cmd+shift+p` (macOS) or `ctrl+shift+p` (windows). Search for `Shell Command: Install 'code' command in PATH command.`, then click that.

VSCode's power lies in its extremely keyboard-centric interface as well as its extensive library of extensions. When in doubt just use the **command palette** `cmd+shift+p` (macOS) `ctrl+shift+p` (windows) to search for anything you're trying to do. For now, open it up and search "install extensions" to install the following extensions:
- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)
- [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
- [Ruff](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff)

Finally you can try creating a new Jupyter notebook and choosing `201b` as the kernel to see if everything is working!

### Optional goodies

You might consider applying for a free [Github student account](https://docs.github.com/en/education/explore-the-benefits-of-teaching-and-learning-with-github-education/github-education-for-students/apply-to-github-education-as-a-student) which gives you access to a variety of additional resources and tools (e.g. using your VSCode setup remotely, using Github actions to run code automatically, etc)

