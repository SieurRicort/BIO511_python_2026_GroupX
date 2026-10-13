#!/usr/bin/env python3

# Import modules
from plotnine import *
import pandas as pd

# Transform data in dataframe
CNV = pd.read_csv("/home/sacha/GITHUB/BIO511_python_2026_GroupX/prac6/sacha/CNV_log2_skin_melanoma.csv")
CNV_clean = CNV.dropna(subset=["chromosome", "cnv_log2"])

# Sort by chromosome
chromosome_order = [str(i) for i in range(1, 23)] + ["X"]

CNV_clean["chromosome"] = pd.Categorical(
    CNV_clean["chromosome"].astype(str),
    categories=chromosome_order,
    ordered=True
)

CNV_clean=CNV_clean.sort_values("chromosome")

CNV_log2 = (
    CNV_clean.groupby("chromosome")["cnv_log2"]
    .describe()
    .reset_index()
)
print(CNV_log2)

# Plot

CNV_log2_fig1=(
    ggplot(
        CNV_clean,
        aes(x="chromosome", y="cnv_log2", fill="chromosome")
    )
    + geom_violin()
    + labs(
    title="CNV log(2) by chromosome",
    x="Chromosome",
    y="CNV log(2)"
    )
    + theme_minimal()
)

CNV_log2_fig1.save(
    "CNV_log2.jpg",
    dpi=300
)