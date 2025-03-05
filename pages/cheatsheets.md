# Coding Cheatsheets

```{tip}
When you're working in Python it can be *super* helpful to regularly refer to these resources. Remember that you can always use any `API reference` link below to get a comprehensive list of *all* the functions and methods in a library - a bit nicer than only relying on `?` in your notebook.
```

## Course Packages
Throughout the course we've been making use of the following Python libraries in case you want to create a reproducible environment for yourself:

- [`numpy`](https://numpy.org/doc/stable/index.html)
- [`scipy`](https://scipy.org/) 
- [`matplotlib`](https://matplotlib.org/)
- [`seaborn`](https://seaborn.pydata.org/)
- [`polars`](https://docs.pola.rs/user-guide/getting-started/)
- [`statsmodels`](https://www.statsmodels.org/stable/user-guide.html)
- [`marginaleffects`](https://marginaleffects.com/)
- [`pymer4`](https://eshinjolly.com/pymer4/)
- [`ipywidgets`](https://ipywidgets.readthedocs.io/en/stable/) - *optional just for interactive demos*


## Computing Basics
- [Terminal commands cheatsheet](https://www.git-tower.com/blog/media/pages/posts/command-line-cheat-sheet/64337e6bae-1733170994/command-line-cheat-sheet-large01.avif)
- [Git & Github cheatsheet](/pages/git)
- [More Git commands](https://education.github.com/git-cheat-sheet-education.pdf)

## Coding Notebooks 
- [Python Notebooks in VSCode](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)
- [Python Notebooks in JupyterLab](https://jupyterlab.readthedocs.io/en/latest/user/notebook.html)
- To show multiple outputs from a single cell add this to the top of your notebook:
  - `%config InteractiveShell.ast_node_interactivity = "all" `
  - Other options include `last`, `last_expr` (default), `last_expr_or_assign`, `none`
- To produce higher-resolution plots add this to the top of your notebook:
  - `%config InlineBackend.figure_formats = 'retina'`


## Conda Environments
- [Conda overview and basic commands](https://nbis-reproducible-research.readthedocs.io/en/course_2104/conda/)
- [Conda and sharing Python environments for reproducible research](https://rse.shef.ac.uk/conda-environments-for-effective-and-reproducible-research/04-sharing-environments/index.html)
- [Conda command cheatsheet](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf)

## Python Basics
- [Basics cheatsheet](https://media.datacamp.com/legacy/image/upload/v1694526244/Marketing/Blog/Python_Basics_Cheat_Sheet-updated.pdf)
- [Interactive Reference](https://www.pythoncheatsheet.org/cheatsheet/basics)
- [Python for R users](https://cran.r-project.org/web/packages/reticulate/vignettes/python_primer.html)

## Numpy - numerical array library
- [Numpy tutorials](https://numpy.org/numpy-tutorials/)
- [Numpy API reference](https://numpy.org/doc/stable/reference/index.html)
- [Numpy Cheatsheet](https://media.datacamp.com/legacy/image/upload/v1676302459/Marketing/Blog/Numpy_Cheat_Sheet.pdf)
- [Numpy for MATLAB users](https://numpy.org/doc/stable/user/numpy-for-matlab-users.html)

## Matplotlib - basic plotting library
- [Matplotlib user guide](https://matplotlib.org/stable/users/index.html)
- [Matplotlib API reference](https://matplotlib.org/stable/api/index.html)
- [Matplotlib tutorials](https://matplotlib.org/stable/tutorials/index.html)
- [Matplotlib cheatsheets](https://matplotlib.org/cheatsheets/)

## Scipy - scientific functions and statistics library
- [SciPy user guide](https://docs.scipy.org/doc/scipy/tutorial/index.html)
- [SciPy API reference](https://docs.scipy.org/doc/scipy/reference/index.html)
- [Summary statistics](https://docs.scipy.org/doc/scipy/reference/stats.html#summary-statistics)
- [Resampling, i.e. montecarlo, bootstrap, permutation](https://docs.scipy.org/doc/scipy/reference/stats.html#resampling-and-monte-carlo-methods)
- [Hypothesis testing](https://docs.scipy.org/doc/scipy/reference/stats.html#hypothesis-tests-and-related-functions)

## Polars - DataFrame and tidy-data analysis library
- [Polars user guide](https://docs.pola.rs/)
- [Polars API reference](https://docs.pola.rs/api/python/dev/reference/index.html)
- [Tidyverse and Polars side-by-side](https://robertmitchellv.com/blog/2022-07-r-python-side-by-side/r-python-side-by-side.html)
- [Polars Rgonomic patterns](https://www.emilyriederer.com/post/py-rgo-polars/)
- [Pandas - alternative DataFrame library we're NOT using](https://pandas.pydata.org/docs/index.html)

## Seaborn - statistical visualization library
- [Seaborn user guide](https://seaborn.pydata.org/tutorial.html)
- [Seaborn API](https://seaborn.pydata.org/api.html)
- [Seaborn cheatsheet](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Python_Seaborn_Cheat_Sheet.pdf)

## Statsmodels - regression library
- [Using formulas in statsmodels](https://www.statsmodels.org/stable/example_formulas.html)
- [OLS model reference](https://www.statsmodels.org/stable/generated/statsmodels.regression.linear_model.OLS.html#statsmodels.regression.linear_model.OLS)
- [Regression results reference](https://www.statsmodels.org/stable/generated/statsmodels.regression.linear_model.RegressionResults.html#statsmodels.regression.linear_model.RegressionResults)
- [Post-hoc pairwise tests](https://www.statsmodels.org/stable/dev/generated/statsmodels.base.model.GenericLikelihoodModelResults.t_test_pairwise.html#statsmodels.base.model.GenericLikelihoodModelResults.t_test_pairwise)
- [`anova_lm` for model comparison](https://www.statsmodels.org/stable/generated/statsmodels.stats.anova.anova_lm.html#statsmodels.stats.anova.anova_lm)

## MarginalEffects - like `emmeans` in R
- [Predictions & Average Predictions](https://marginaleffects.com/man/python/predictions.html)

## Pymer4 - multi-level/linear-mixed-models
- [Pymer4 Usage Guide](https://eshinjolly.com/pymer4/auto_examples/index.html)
- [Repeated Measures Overview](https://eshinjolly.com/2019/02/18/rep_measures/)
- [`.fit()` method reference](https://eshinjolly.com/pymer4/api.html#pymer4.models.Lmer.fit)
- [`.post_hoc()` method reference](https://eshinjolly.com/pymer4/api.html#pymer4.models.Lmer.post_hoc)

<!-- ## Advanced stats + machine learning
- [Scikit-learn cheatsheet](https://media.datacamp.com/legacy/image/upload/v1676302389/Marketing/Blog/Scikit-Learn_Cheat_Sheet.pdf)
  - [Supervised learning](https://scikit-learn.org/stable/supervised_learning.html)
  - [Decomposition](https://scikit-learn.org/stable/modules/decomposition.html)
  - [Model selection & evaluations](https://scikit-learn.org/stable/model_selection.html)
- [Pymer4 (LMMs) tutorials](https://eshinjolly.com/pymer4/auto_examples/index.html) -->
