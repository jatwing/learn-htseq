import pandas as pd
# Input: raw count matrix and gene lengths
raw_counts = pd.DataFrame({'Gene1': [100, 200], 'Gene2': [300, 400]}, index=['Sample1', 'Sample2'])
gene_lengths = pd.Series({'Gene1': 1000, 'Gene2': 2000})  # in base pairs
# Convert gene lengths to kilobases
gene_lengths_kb = gene_lengths / 1000
# Calculate RPK
rpk = raw_counts.div(gene_lengths_kb, axis=1)
# For FPKM
total_rpk = rpk.sum(axis=1)
fpkm = rpk.div(total_rpk, axis=0) * 1e6
# For TPM
sum_rpk = rpk.sum(axis=1)
tpm = rpk.div(sum_rpk, axis=0) * 1e6
print("FPKM:\n", fpkm)
print("TPM:\n", tpm)