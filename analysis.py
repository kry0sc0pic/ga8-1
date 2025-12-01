# Interactive notebook demo for marimo
# Author email (per instructions): 23f2000764@ds.study.iitm.ac.in

import marimo

app = marimo.App()


@app.cell
def _():
    """
    Import core libraries and expose them as cell outputs.

    Data flow:
    - Provides `mo`, `np`, `pd` to downstream cells.
    """
    import marimo as mo
    import numpy as np
    import pandas as pd

    return mo, np, pd


@app.cell
def _(mo):
    """
    High-level documentation cell.

    This markdown explains the purpose of the notebook so that it is
    self-documenting for other researchers.
    """
    mo.md(
        r"""
        # Interactive Relationship Explorer (Marimo)

        This notebook demonstrates an **interactive** and **reproducible** workflow
        using **marimo**, a reactive Python notebook.

        We generate a synthetic dataset with two variables, `x` and `y`, where:
        - `y` is a noisy linear function of `x`.
        - A **slider widget** controls the amount of noise.
        - As noise increases, the **correlation between `x` and `y` decreases**.

        The notebook illustrates:

        - Cell-level **dependencies** for transparent data flow  
        - **Interactive widgets** that recalculate results reactively  
        - **Dynamic markdown** that updates based on widget state  
        """
    )


@app.cell
def _(mo):
    """
    UI controls cell.

    Data flow:
    - Exposes `noise_slider` as an output.
    - Downstream cells recompute when `noise_slider.value` changes.
    """
    noise_slider = mo.ui.slider(
        start=0,
        stop=100,
        value=20,
        label="Noise level (%)",
        step=5,
    )

    mo.hstack(
        [
            mo.md("### Controls"),
            noise_slider,
        ]
    )

    return noise_slider,


@app.cell
def _(np, pd, noise_slider):
    """
    Synthetic data generation cell.

    Data flow:
    - Inputs: `np`, `pd` (from imports), `noise_slider` (from controls).
    - Output: `df` (DataFrame) that downstream analysis and visualization cells use.

    When `noise_slider.value` changes:
    - Noise scale is updated
    - New data are generated
    - All dependent cells recompute automatically
    """
    n_samples = 300
    rng = np.random.default_rng(42)

    # Base signal: x ~ N(0, 1)
    x = rng.normal(0.0, 1.0, size=n_samples)

    # Convert slider percentage to noise standard deviation
    noise_scale = 0.1 + (noise_slider.value / 100) * 1.5
    noise = rng.normal(0.0, noise_scale, size=n_samples)

    # Linear relationship with noise
    y = 2.0 * x + noise

    df = pd.DataFrame({"x": x, "y": y})

    return df, noise_scale


@app.cell
def _(df, noise_slider, noise_scale, mo):
    """
    Summary statistics and dynamic markdown.

    Data flow:
    - Inputs: `df`, `noise_slider`, `noise_scale`.
    - Computes correlation between x and y.
    - Emits dynamic markdown that reflects widget state and analysis results.
    """
    corr = df["x"].corr(df["y"])

    # Create a qualitative indicator based on correlation strength
    strength = abs(corr)
    if strength > 0.9:
        quality = "Very strong"
        dots = "🟢" * 5
    elif strength > 0.7:
        quality = "Strong"
        dots = "🟢" * 4 + "⚪"
    elif strength > 0.4:
        quality = "Moderate"
        dots = "🟡" * 3 + "⚪⚪"
    else:
        quality = "Weak"
        dots = "🔴" * 2 + "⚪⚪⚪"

    mo.md(
        f"""
        ## Relationship summary (reactive)

        - **Noise level:** `{noise_slider.value}%`  
        - **Noise scale (σ):** `{noise_scale:.3f}`  
        - **Correlation (x, y):** `{corr:.3f}`  

        **Qualitative interpretation:** {quality} relationship  
        {dots}

        As you increase the noise slider, the points spread out more and the
        correlation magnitude decreases. This simulates how measurement noise
        or unobserved factors weaken observable relationships between variables.
        """
    )


@app.cell
def _(df, mo):
    """
    Simple data preview cell.

    Data flow:
    - Input: `df` from the synthetic data cell.
    - Output: a small preview table for quick inspection.
    """
    mo.md("### Data preview (first 10 rows)")
    df.head(10)


if __name__ == "__main__":
    app.run()
