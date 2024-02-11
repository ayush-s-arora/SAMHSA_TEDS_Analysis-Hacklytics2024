import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer


# Process data into CSV
TEDSdf = pd.concat(map(pd.read_csv, ['tedsa_puf_2016.csv', 'tedsa_puf_2017.csv', 'tedsa_puf_2018.csv', 'tedsa_puf_2019.csv', 'tedsa_puf_2020.csv', 'tedsa_puf_2021.csv']), ignore_index=True)

TEDSdf = TEDSdf[['AGE', 'ARRESTS', 'SUB1', 'MARSTAT', 'EDUC', 'PRIMINC', 'DAYWAIT', 'FREQ1', 'FREQ_ATND_SELF_HELP', 'HLTHINS', 'FRSTUSE1', 'RACE', 'SERVICES', 'PSYPROB', 'NOPRIOR']]

TEDSdf = TEDSdf.drop(TEDSdf[TEDSdf.eq(-9).any(axis=1)].index)

TEDSdf.to_csv('CleanedCombinedTEDS.csv', index=False)


# Random Forest Classifier
X = TEDSdf[['AGE', 'ARRESTS', 'SUB1', 'MARSTAT', 'EDUC', 'PRIMINC', 'DAYWAIT', 'FREQ1', 'FREQ_ATND_SELF_HELP', 'HLTHINS', 'FRSTUSE1', 'RACE', 'SERVICES', 'PSYPROB']]
y = TEDSdf['NOPRIOR']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

categorical_features = ['SUB1', 'MARSTAT', 'EDUC', 'PRIMINC', 'FREQ1', 'HLTHINS', 'FRSTUSE1', 'RACE', 'SERVICES', 'PSYPROB']
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),  # Impute missing values
    ('onehot', OneHotEncoder(handle_unknown='ignore'))     # One-hot encode categorical features
])

preprocessor = ColumnTransformer(
    transformers=[
        ('cat', categorical_transformer, categorical_features),
    ])

pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                           ('classifier', RandomForestClassifier(random_state=42))])

pipeline.fit(X_train, y_train)

y_pred = pipeline.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)