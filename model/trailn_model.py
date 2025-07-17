import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

# Example dataset loading and processing
df = pd.read_csv("lead_data.csv")

# Encoding categorical features
label_enc = LabelEncoder()
df['family'] = label_enc.fit_transform(df['Family Background'])
df['age'] = label_enc.fit_transform(df['Age Group'])

X = df[['Credit Score', 'Income', 'family', 'age']]  # Use relevant features
y = df['Intent']  # Binary intent: 0 = low, 1 = high

# Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = GradientBoostingClassifier()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "../backend/model.pkl")