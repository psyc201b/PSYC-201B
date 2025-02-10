# %%
# Imports
import numpy as np
import polars as pl
from polars import col
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import f
import ipywidgets as widgets

# %%
# Data
# df = pl.read_csv("./data/internet.csv")

# Globals
# X = df['SES'].cast(int).to_numpy()
# y = df['Internet'].cast(int).to_numpy()

# TRUE_MEAN = y.mean()

figsize = (8,4)

# %%
# Helpers
def loss_function(guess, y):
    return np.sum((y - guess) ** 2)


# %%
# Mean SSE
def mean_model_widget():


    # Data
    np.random.seed(42)

    true_intercept = 1

    start_guess = 1.8
    guess_min = 0
    guess_max = 2
    step = .1

    X = np.random.rand(100)
    y = true_intercept + np.random.normal(0, .5, size=100)

    y_pred = true_intercept

    true_sse = np.sum((y - y_pred) ** 2)


    def update_plot(guess):

        # Regression line based on guessed slope
        y_pred = guess 
        sse = np.sum((y - y_pred) ** 2)


        # For color switching
        correct = sse - true_sse == 0 
        color = 'red' if not correct else 'green'
        error_color = 'gray' if not correct else 'green'
        beta_1 = r'$\beta_0$'
        x_1 = r'$X_1$'
        y_text = r'$y$'

        # Init plot
        f, axs = plt.subplots(1, 2, figsize=figsize)

        # Left 
        axs[0].scatter(X, y, color='k', s=10)
        axs[0].axhline(y=guess, color=color)
        axs[0].set(title=f'Estimated {beta_1} (Mean): {guess:.2f}', xlabel=f"{x_1}", ylabel=f"{y_text}")

        for x_i, y_i in zip(X, y):
            axs[0].vlines(x=x_i, ymin=min(y_i, guess), ymax=max(y_i, guess), color=error_color, linestyle='--', alpha=.25)

        # Right
        # Loss on this guess
        mse = loss_function(guess, y)
        # Generate errors
        guesses = np.linspace(guess_min, guess_max, 100)
        losses = [loss_function(g,y) for g in guesses]

        axs[1].plot(guesses, losses, color='gray', label='Squared-Errors')
        axs[1].scatter([guess], [mse], color=color, s=80, label='Estimate')
        axs[1].set(xlabel=f'Estimated {beta_1} (Mean)', xlim=(guess_min, guess_max), ylabel='Sum of Squared-Errors', title='Model Prediction Error')
        axs[1].legend()

        plt.tight_layout()
        plt.show()



    def make_widget():
        "Create interactive widget for mean model"

        mean_slider = widgets.FloatSlider(
            value=start_guess,
            min=guess_min,
            max=guess_max,
            step=step,
            description='Mean:',
            continuous_update=True
        )
        # Display interactive plot
        return widgets.interactive(update_plot, guess=mean_slider)
    
    return make_widget()
# %%

# Slope SSE
def slope_model_widget():


    # Data
    np.random.seed(42)

    true_slope = 2
    true_intercept = 1

    start_guess = 1
    guess_min = 0.5
    guess_max = 3.4
    step = .1

    X = np.random.rand(100)
    y = true_intercept + true_slope * X + np.random.normal(0, .5, size=100)

    y_pred = true_intercept + true_slope * X

    true_sse = np.sum((y - y_pred) ** 2)


    def update_plot(guess):

        # Regression line based on guessed slope
        y_pred = true_intercept + guess * X
        sse = np.sum((y - y_pred) ** 2)


        # For color switching
        correct = sse - true_sse == 0 
        color = 'red' if not correct else 'green'
        error_color = 'gray' if not correct else 'green'
        beta_1 = r'$\beta_1$'
        x_1 = r'$X_1$'
        y_text = r'$y$'

        # Init plot
        f, axs = plt.subplots(1, 2, figsize=figsize)

        # Left 
        axs[0].scatter(X, y, color='k', s=10)
        axs[0].plot(X, y_pred, color=color)
        axs[0].set(title=f'Estimated {beta_1} (Slope): {guess:.2f}', xlabel=f"{x_1}", ylabel=f"{y_text}")

        for x_i, y_i, y_hat_i in zip(X, y, y_pred):
            axs[0].vlines(x=x_i, ymin=min(y_i, y_hat_i), ymax=max(y_i, y_hat_i), color=error_color, linestyle='--', alpha=.25)

        # Right
        # Loss on this guess
        mse = loss_function(guess, y)
        # Generate errors
        guesses = np.linspace(guess_min, guess_max, 100)
        losses = [loss_function(g,y) for g in guesses]

        axs[1].plot(guesses, losses, color='gray', label='Squared-Errors')
        axs[1].scatter([guess], [mse], color=color, s=80, label='Estimate')
        axs[1].set(xlabel=f'Estimated {beta_1} (Slope)', xlim=(guess_min, guess_max), ylabel='Sum of Squared-Errors', title='Model Prediction Error')
        axs[1].legend()

        plt.tight_layout()
        plt.show()



    def make_widget():
        "Create interactive widget for mean model"

        mean_slider = widgets.FloatSlider(
            value=start_guess,
            min=guess_min,
            max=guess_max,
            step=step,
            description='Slope:',
            continuous_update=True
        )
        # Display interactive plot
        return widgets.interactive(update_plot, guess=mean_slider)
    
    return make_widget()
# %%
# Both 
def univariate_regression_widget():


    # Data
    np.random.seed(42)

    true_slope = 2.
    true_intercept = 1.

    start_intercept = 1.8
    guess_intercept_min = 0.5
    guess_intercept_max = 3.4

    start_slope = 1
    guess_slope_min = 0.5
    guess_slope_max = 3.4
    step = .1

    X = np.random.rand(100)
    y = true_intercept + true_slope * X + np.random.normal(0, .5, size=100)

    y_pred = true_intercept + true_slope * X

    true_sse = np.sum((y - y_pred) ** 2)


    def update_plot(guess_intercept, guess_slope):

        # Regression line based on guessed slope
        y_pred = guess_intercept + guess_slope * X
        sse = np.sum((y - y_pred) ** 2)


        # For color switching
        correct = sse - true_sse == 0 
        color = 'red' if not correct else 'green'
        error_color = 'gray' if not correct else 'green'
        beta_0 = r'$\beta_0$'
        beta_1 = r'$\beta_1$'
        x_1 = r'$X_1$'
        y_text = r'$y$'

        # Init plot
        f, ax = plt.subplots(1, 1, figsize=figsize)

        if guess_intercept == true_intercept and guess_slope == true_slope:
            title = f"Estimated {beta_0} (Intercept): {guess_intercept:.2f} Correct!\nEstimated {beta_1} (Slope): {guess_slope:.2f} Correct!"
        elif guess_intercept == true_intercept:
            title = f"Estimated {beta_0} (Intercept): {guess_intercept:.2f} Correct!\nEstimated {beta_1} (Slope): {guess_slope:.2f}"
        elif guess_slope == true_slope:
            title = f"Estimated {beta_0} (Intercept): {guess_intercept:.2f}\nEstimated {beta_1} (Slope): {guess_slope:.2f} Correct!"
        else:
            title = f"Estimated {beta_0} (Intercept): {guess_intercept:.2f}\nEstimated {beta_1} (Slope): {guess_slope:.2f}"

        # Left 
        ax.scatter(X, y, color='k', s=10)
        ax.plot(X, y_pred, color=color)
        ax.set(
            title=title,
            xlabel=f"{x_1}", 
            ylabel=f"{y_text}"
        )

        for x_i, y_i, y_hat_i in zip(X, y, y_pred):
            ax.vlines(x=x_i, ymin=min(y_i, y_hat_i), ymax=max(y_i, y_hat_i), color=error_color, linestyle='--', alpha=.25)

        plt.tight_layout()
        plt.show()



    def make_widget():
        "Create interactive widget for mean model"

        intercept_slider = widgets.FloatSlider(
            value=start_intercept,
            min=guess_intercept_min,
            max=guess_intercept_max,
            step=step,
            description='Intercept:',
            continuous_update=True
        )

        slope_slider = widgets.FloatSlider(
            value=start_slope,
            min=guess_slope_min,
            max=guess_slope_max,
            step=step,
            description='Slope:',
            continuous_update=True
        )
        # Display interactive plot
        return widgets.interactive(update_plot, guess_intercept=intercept_slider, guess_slope=slope_slider)
    
    return make_widget()

def plot_F_sampling_distribution(PRE, F, pval, pa, pc, n):

    # Generate values for plotting the F-distribution
    x = np.linspace(0, F + 2, 1000)
    y = f.pdf(x, pa - pc, n)

    # Print results
    print(f"Proportion Reduction of Error: {PRE:.3f}, F = {F:.3f}, p = {pval:.4f}")

    # Create the plot
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label=f'F({pa - pc}, {n - pa}) distribution', color='blue')

    # Fill under the curve up to the critical value
    plt.fill_between(x, y, where=(x >= F), color='red', alpha=0.3, label="Rejection Region")

    # Add vertical lines
    # plt.axvline(F, color='red', linestyle='--', label=f'Critical F = {F_crit:.3f}')
    plt.axvline(F, color='black', linestyle=':', label=f'Observed F = {F:.3f}')

    # Labels and title
    plt.xlabel('F-value')
    plt.ylabel('Density')
    plt.title('Sampling Distribution of F')
    plt.legend()
    plt.show()
