from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import pandas as pd

# Process data into CSV
TEDSdf = pd.read_csv('CleanedCombinedTEDS.csv')
# 1. Encode Categorical Variables (if needed)

# 2. Choose a Distance Metric (Hamming distance for categorical data)
# Assuming X is your feature matrix and y is your target variable
X_categorical = TEDSdf[['SUB1', 'MARSTAT', 'EDUC', 'PRIMINC', 'FREQ1', 'FREQ_ATND_SELF_HELP', 'HLTHINS', 'FRSTUSE1', 'RACE', 'SERVICES', 'PSYPROB']]
X_numerical = TEDSdf[['AGE', 'ARRESTS', 'DAYWAIT']]
y = TEDSdf['NOPRIOR']

# 3. Scale Numerical Variables (if necessary)
scaler = StandardScaler()
X_numerical_scaled = scaler.fit_transform(X_numerical)

# Combine scaled numerical features and categorical features
import numpy as np
X_combined = np.hstack((X_numerical_scaled, X_categorical))

# 4. Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X_combined, y, test_size=0.2, random_state=42)

# 5. Implement kNN Algorithm
k = 5  # Number of neighbors
knn = KNeighborsClassifier(n_neighbors=k, metric='hamming')
knn.fit(X_train, y_train)

# 6. Predict on test data
y_pred = knn.predict(X_test)

# 7. Evaluate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
