# PSYC 201B: Statistical Intuitions for Social Scientists

Source code for course website, builty using [JupyterBook](https://jupyterbook.org/en/stable/).

## Instructions for editing and updating course pages and notebooks

After cloning the repo create a new conda environment for the course following the instructions below.

*If you're editing lots of materials please make a new git branch and open a PR against the `main` branch. Otherwise, you can just edit the files directly in the `main` branch.*

### Creating/Modifying labs & lectures

The course materials you'll mostly be working with are stored in the `labs/` and `lectures/` folders. Within each folder, materials are organized into sub-folder by week (lectures) or number (labs), e.g. `labs/1/` and `lectures/wk1/`. Each sub-folder contains a `overview.md` file, which is organized using [markdown directives](https://jupyterbook.org/en/stable/content/myst.html) to highlight the *topic*, *readings*, and *resources* for that week's lab or lecture.

You'll primarily be adding/removing/editing the `.md` and `.ipynb` files in these directories. For labs, you can create new `.md` and `.ipynb` files in the sub-folder that we'll go through together with students. For lectures, I'll plan to using additional `.md` files to embed course slides and additional notes/faqs each week. 

You'll want to make sure any files you've created or edited are are referenced in the table-of-contents `_toc.yml`. This file controls both *what* and the *order* of how files are rendered. You can also hide work-in-progress files by using commented lines in `_toc.yml`. You can see how I've done this with other files in the repo.

To see your changes, you should build and preview the website locally by running `jupyter-book build .` and `open _build/html/index.html` in your terminal. If you run into issues you can always wipe the `_build/` folder by running `jupyter-book clean .` and then rebuild.

Once you're finished, just commit and push your changes to github or open a pull-request against the `main` branch. The course website is automatically updated and deployed whenever we push or merge changes to the `main` branch!

### Creating/Modiying course pages

In addition to labs & lectures we may also want to create/edit new course pages. This can be done by adding/editing the `.md` files in the `pages/` folder and updating the table-of-contents `_toc.yml` file accordingly. 

## Development instructions

### One-time environment setup
- `conda create -n 201b python=3.11 pip ruff ipykernel jupyter-book -c conda-forge`
- `conda activate 201b`
- `conda install pymer4 -c ejolly -c conda-forge -c defaults`
- `pip install -r requirements.txt`

### Using environment
- `conda activate 201b`
- `jupyter-book build .`
- `open _build/html/index.html`
