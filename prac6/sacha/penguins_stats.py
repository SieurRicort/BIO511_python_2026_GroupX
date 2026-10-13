#!/usr/bin/env python3

# Import modules
from plotnine import *
import pandas as pd
import seaborn as sns

# Get the dataset
peng=sns.load_dataset("penguins")
peng_clean = peng.dropna(subset=["island", "body_mass_g"])

# Group by island
body_island = (
    peng_clean.groupby("island")
    .agg(mean=("body_mass_g", "mean"),std=("body_mass_g", "std"))
    .reset_index()
)

body_island2 = (
    peng_clean.groupby("island")["body_mass_g"]
    .describe()
    .reset_index()
)

# Plot

Penguin_fig3_plotnine=(
    ggplot(
        body_island2,
        aes(x="island", y="mean", fill="island")
    )
    + geom_col()
    + geom_errorbar(
        aes(ymin="mean - std", ymax="mean + std"),
        width=0.2
    )
    + labs(
    title="Mean penguin body mass by island",
    x="Island",
    y="Body mass (g)",
    fill="Island"
    )
    + scale_fill_manual(
    values={
        "Biscoe": "#0051FF",
        "Dream": "#0066FF",
        "Torgersen": "#00AAFF"
    },
    name="Island"
    )
    + theme_minimal()
)

Penguin_fig3_plotnine.save(
    "Penguin_body-mass_island.jpg",
    dpi=300
)