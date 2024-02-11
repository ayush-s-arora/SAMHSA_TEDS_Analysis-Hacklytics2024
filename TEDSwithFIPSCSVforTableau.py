import pandas as pd
import numpy as np

TEDSdf = pd.concat(map(pd.read_csv, ['tedsa_puf_2010.csv', 'tedsa_puf_2011.csv', 'tedsa_puf_2012.csv', 'tedsa_puf_2013.csv', 'tedsa_puf_2014.csv', 'tedsa_puf_2015.csv', 'tedsa_puf_2016.csv', 'tedsa_puf_2017.csv', 'tedsa_puf_2018.csv', 'tedsa_puf_2019.csv', 'tedsa_puf_2020.csv', 'tedsa_puf_2021.csv']), ignore_index=True)

TEDSdf = TEDSdf[['AGE', 'ARRESTS', 'STFIPS', 'SUB1', 'MARSTAT', 'EDUC', 'PRIMINC', 'DAYWAIT', 'FREQ1', 'FREQ_ATND_SELF_HELP', 'HLTHINS', 'FRSTUSE1', 'RACE', 'SERVICES', 'PSYPROB', 'NOPRIOR']]

# TEDSdf = TEDSdf.drop(TEDSdf[TEDSdf.eq(-9).any(axis=1)].index)

TEDSdf.to_csv('CleanedCombinedTEDSFIPS.csv', index=False)