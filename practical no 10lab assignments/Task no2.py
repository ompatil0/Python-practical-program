import pandas as pd

data = {
    "State": ["MH","GJ","RJ","UP","MP"],
    "Area": [307713,196024,342239,243286,308245],
    "Population": [12,7,8,20,9]   # in crores (simple)
}

df = pd.DataFrame(data)

# a) Full info
print(df)

# b) Largest area
print("Largest Area:", df.loc[df["Area"].idxmax()]["State"])

# c) Largest population
print("Largest Population:", df.loc[df["Population"].idxmax()]["State"])

# d) Population density
df["Density"] = df["Population"] / df["Area"]
print(df)

# e) Highest density
print("Highest Density:", df.loc[df["Density"].idxmax()]["State"])