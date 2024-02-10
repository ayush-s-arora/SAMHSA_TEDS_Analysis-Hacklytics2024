import pandas as pd
import numpy as np

year = 2016
TEDSdf = pd.DataFrame()
for year in range(2016, 2022):
    TEDSdf.append = pd.read_csv(f'tedsa_puf_{year}.csv')

print(TEDSdf)