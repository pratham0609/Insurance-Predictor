import numpy as np 
import pandas as pd
from sklearn.preprocessing import LabelEncoder

main_df = pd.read_csv("insurance.csv")
main_df.head()
# main_df.describe()
main_df.isna().sum()