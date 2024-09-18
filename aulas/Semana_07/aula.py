def x():
    print("\n")

import pandas as pd

filepath = "vgsales.csv"
df = pd.read_csv(filepath, sep=",")
print(df)
df_json = pd.read_json("vgsales.json")
print(df_json)

x()

a = [
    {"col1": 1, "col2":True},
    {"col1": 2, "col2": False}
]
b = {
    "col1":[1,2],
    "col2":[True,False]
}

x()

print(a)
print(b)

x()

df = pd.DataFrame(b)
print(df)

x()

records = [
    (1, True, 0.0),
    (2, False, "Hello")
]
df = pd.DataFrame(records, columns=["Col1", "Col2", "Col3"])

print(df)

x()
df = pd.read_csv(filepath, sep=",")
print(df.index)
x()
print(df.columns)
x()
print(df.shape)
x()
print(df.dtypes)
x()

columns = ["Name", "Genre", "Platform"]
sub_df = df[columns]
sub_df2 = sub_df.set_index("Name")
print(sub_df2)

x()
print(sub_df2.loc["Pokemon Red/Pokemon Blue"])

x()
print(sub_df[sub_df["Name"] == "Pokemon Red/Pokemon Blue"])

x()
print(df[df["Global_Sales"]>= 1.0])

x()
print(df)
head_df = df.head().copy()
head_df["type"] = ["Retro", "Retro", "Modern",  "Modern", "Modern"]
print(head_df)

x()
head_df.drop("type", axis=1, inplace=True)
print(head_df)

x()
print("SUB DF NOVO")
sub_df = sub_df.copy()

new_row = {
    "Name": "Mario Demo",
    "Genre": "Plataform",
    "Platform": "Switch 2",
}
new_df = pd.DataFrame([new_row])
print(new_df)
x()
print(pd.concat([df,new_df], ignore_index=True))

x()
print(df.describe())

