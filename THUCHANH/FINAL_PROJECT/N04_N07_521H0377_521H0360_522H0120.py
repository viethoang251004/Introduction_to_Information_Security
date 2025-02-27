import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

# Step 1: Load the data
data = pd.read_csv('urldata.csv')

# Step 2: Encode the target variable
label_encoder = LabelEncoder()
data['Label'] = label_encoder.fit_transform(data['Label'])

# Step 3: Split the data into features (X) and target variable (y)
X = data.drop(['Domain', 'Label'], axis=1)
y = data['Label']

# Split data into training and testing sets for validation
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Train the Random Forest model
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier.fit(X_train, y_train)

# Evaluate the model
y_pred = rf_classifier.predict(X_test)
print("Model Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Print feature importance
feature_importance = pd.DataFrame(rf_classifier.feature_importances_, index=X.columns, columns=['importance']).sort_values('importance', ascending=False)
print("Feature Importance:")
print(feature_importance)

# Function to check if domain exists and predict its legality
def predict_domain_legality(domain):
    if domain in data['Domain'].values:
        domain_row = data[data['Domain'] == domain].drop(['Domain', 'Label'], axis=1)
        print("Domain Row:")
        print(domain_row)
        prediction = rf_classifier.predict(domain_row)
        print("Prediction:", prediction)
        if prediction[0] == 1:
            print(f"The domain '{domain}' is likely a phishing domain.")
        else:
            print(f"The domain '{domain}' is likely a legitimate domain.")
    else:
        print(f"The domain '{domain}' does not exist in the dataset.")

# Prompt user for domain input
domain_to_check = input("Enter a domain to check its legality: ")

# Predict domain legality
predict_domain_legality(domain_to_check)