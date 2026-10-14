# download the dataset

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from plotnine import ggplot, aes, geom_point, labs, ggsave


# 1. Load the penguins dataset
penguins = sns.load_dataset("penguins")
print("Rows before dropna:", len(penguins))

# Remove rows with missing values
penguins = penguins.dropna()
print("Rows after dropna:", len(penguins))

print(penguins.head())



# 2. Matplotlib scatterplot
plt.figure()
plt.scatter(penguins["flipper_length_mm"], penguins["body_mass_g"])
plt.title("Flipper length vs body mass in penguins")
plt.xlabel("Flipper length (mm)")
plt.ylabel("Body mass (g)")
plt.savefig("scatter_matplotlib.png")
plt.close()

#Create the same plot but using plotly. Save an interactive file (.html)

# 3. Plotly scatterplot
fig = px.scatter(
    data_frame=penguins,
    x="flipper_length_mm",
    y="body_mass_g",
    title="Flipper length vs body mass in penguins",
    labels={
        "flipper_length_mm": "Flipper length (mm)",
        "body_mass_g": "Body mass (g)",
    },
)
fig.write_html("scatter_plotly.html")




# 4. Seaborn scatterplot, colored by species
plt.figure()
sns.scatterplot(
    data=penguins,
    x="flipper_length_mm",
    y="body_mass_g",
    hue="species",
)
plt.title("Flipper length vs body mass in penguins")
plt.xlabel("Flipper length (mm)")
plt.ylabel("Body mass (g)")
plt.savefig("scatter_seaborn.png")
plt.close()


# 5. Plotnine scatterplot
p = (
    ggplot(penguins, aes(x="flipper_length_mm", y="body_mass_g"))
    + geom_point()
    + labs(
        title="Flipper length vs body mass in penguins",
        x="Flipper length (mm)",
        y="Body mass (g)",
    )
)
ggsave(p, filename="scatter_plotnine.png")



