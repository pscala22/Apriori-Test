import numpy as np
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# Loading the Data
data = pd.read_excel('Online Retail.xlsx')
data.head()
print ("File is observed")