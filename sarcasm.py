import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import BernoulliNB
from sklearn.metrics import classification_report
from imblearn.over_sampling import SMOTE
from sklearn.ensemble import RandomForestClassifier

# Load the dataset
data = pd.read_json("Sarcasm.json", lines=True)

# Map the target variable to human-readable labels
data["is_sarcastic"] = data["is_sarcastic"].map({0: "Not Sarcasm", 1: "Sarcasm"})
data = data[["headline", "is_sarcastic"]]

# Split the data into input and target variables
headlines = np.array(data["headline"])
y = np.array(data["is_sarcastic"])

cv = CountVectorizer()
X = cv.fit_transform(headlines)

# Balance the dataset by oversampling the minority class (sarcastic headlines)
oversampler = SMOTE()
X, y = oversampler.fit_resample(X, y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

# Initialize and fit the model
model = RandomForestClassifier(n_estimators=100, max_depth=20, min_samples_leaf=5, random_state=42)
model.fit(X_train, y_train)

# Evaluate the model using precision, recall, and F1-score
y_pred = model.predict(X_test)
print(y_pred)
report = classification_report(y_test, y_pred, target_names=["Not Sarcasm", "Sarcasm"])
print(report)

# Allow the user to enter texts and predict whether they are sarcastic or not
while True:
    user_input = input("Enter a headline (press enter to exit): ")
    if user_input == "":
        break
    data = cv.transform([user_input]).toarray()
    output = model.predict(data)
    print("Prediction:", output[0])


