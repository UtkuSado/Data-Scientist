import seaborn as sns 

planets = sns.load_dataset("planets")
df = planets.copy()

df_num = df.select_dtypes(include= ["float64", "int64"])
print(df_num.head())