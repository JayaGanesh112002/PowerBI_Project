# importing pandas
import pandas as pd

# URL for the source dataset
url = "https://raw.githubusercontent.com/LokeshKumarChauhan/DE_with_powerBI/main/Walmart.csv"

# Reading the dataset into a pandas dataframe
df = pd.read_csv(url)

# Creating a CSV file
df.to_csv("Walmart.CSV")