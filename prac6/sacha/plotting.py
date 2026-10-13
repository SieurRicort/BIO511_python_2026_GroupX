#!/usr/bin/env python3

# Import modules
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from plotnine import *

# Import penguin and remove NAs
peng=sns.load_dataset("penguins")
peng.dropna(how='any',inplace=True)
print(peng.columns.values.tolist()) # Fastest way to print out headers of a df
print(peng['species'].unique()) # Retrieve species names

# Plot data using matplotlib
plt.scatter(peng['flipper_length_mm'], peng['body_mass_g'])
plt.title("Body mass over flipper length")
plt.xlabel("Flipper length (mm)")
plt.ylabel("Body mass (g)")
plt.savefig("Penguin_fig1_matplotlib.png", dpi=300)

# Plot data using plotly

penguin_fig1=px.scatter(
    peng,
    x="flipper_length_mm",
    y="body_mass_g",
    title="Body mass over flipper length"
)
penguin_fig1.write_html('Penguin_fig1_plotly.html')

# Plot using seaborn
species_colors={"Adelie" : "#EA205E", "Chinstrap" : "#2E90E8", "Gentoo" : "#A1C535"}

sns_plot=sns.scatterplot(
    data = peng,
    x='flipper_length_mm',
    y='body_mass_g',
    hue='species',
    palette=species_colors
    )
# It saves parameters of matplotlib set earlier !!!!!
sns_plot.figure.savefig('Penguin_fig1_sns.png', dpi=300)

# Plotnine

Penguin_fig1_plotnine = (
    ggplot(peng, aes(x="flipper_length_mm", y="body_mass_g", color="species"))
    + geom_point()
    + labs(
        title="Flipper length over body mass",
        x="Flipper length (mm)",
        y="Body mass (g)",
        color="Penguin species"
    )
    + scale_color_manual(values=species_colors)
)
Penguin_fig1_plotnine.save(
    "Penguin_fig1_plotnine.jpg",
    dpi=300
)

# Histogram using plotnine

Penguin_fig2_plotnine = (
    ggplot(peng, aes(x="bill_length_mm"))
    + geom_histogram(binwidth=2)
    + labs(
        title="Histogram of bill length (mm)",
        x="Bill length (mm)",
    )
)
Penguin_fig2_plotnine.save(
    "Penguin_fig2_plotnine.jpg",
    dpi=300
)