def X():
    print( "\n")

import pandas as pd

filepath = "steam.csv"
df = pd.read_csv(filepath, sep=",")
print(df.head())
print(df.columns)
print(df.iloc[0])

print(df['All Reviews Summary'].head(20))
print(df['All Reviews Summary'].unique())
print(df['All Reviews Summary'].value_counts())
X()

print(pd.isna(df['All Reviews Summary']).sum())
X()

result = df['All Reviews Summary'] == "Overwhwlmingly Negative"
print(df[result])
X()

subset_df = df[['Release Date','All Reviews Summary']]
print(subset_df.head())
X()

result = subset_df[~result]
print(subset_df.head(20))