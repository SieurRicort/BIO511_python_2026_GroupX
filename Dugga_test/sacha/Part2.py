#!/usr/bin/env python3

# Import modules
import pandas as pd
import sys
from plotnine import *

# 2.1.a
df = pd.read_csv(sys.argv[1])
# python3 Part2.py data.csv

# 2.1.b
top20_df = df.iloc[0:19]
#print(top20_df)

# 2.1.c

top20_long = pd.melt(
    top20_df,
    id_vars=["gene_name"],
    value_vars=["fpkm_unstranded", "tpm_unstranded_int"],
    var_name="method",
    value_name="expression"
)
print(top20_long)
top20_fig1_scatter= (
    ggplot(
        top20_long,
        aes(
            x='gene_name',
            y='expression',
            color='method'
        )
    )
    + geom_point()
    + labs(
        x="Gene name",
        y="Expression (FPKM / TPM)",
        title="FPKM vs TPM for the 20 most highly expressed genes",
        color="Normalization method"
    )
)

top20_fig1_scatter.save(
    "Comparison_method.jpg",
    dpi=300
)

# extra

top20_fig2_scatter= (
    ggplot(
        top20_df,
        aes(
            x='fpkm_unstranded',
            y='tpm_unstranded_int'
        )
    )
    + geom_point()
    + labs(
        x="Expresion FPKM (Fragments Per Kilobase Million)",
        y="Expresion TPM (Transcripts Per Million)",
        title="FPKM vs TPM for the 20 most highly expressed genes"
    )
)

top20_fig2_scatter.save(
    "Comparison_1v1.jpg",
    dpi=300
)