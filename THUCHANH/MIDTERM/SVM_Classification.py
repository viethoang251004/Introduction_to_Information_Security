# Ba mô hình SVM phân loại với các kernel khác nhau:
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import classification_report

# Load the Iris dataset
iris = datasets.load_iris()
X = iris.data
y = iris.target
# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
# Standardize features by removing the mean and scaling to unit variance
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 1. SVM Model with Linear Kernel
model_linear = SVC(kernel='linear')
model_linear.fit(X_train, y_train)
y_pred_linear = model_linear.predict(X_test)
print("Linear Kernel SVM Classification Report:")
print(classification_report(y_test, y_pred_linear))


# 2. SVM Model with Polynomial Kernel
model_poly = SVC(kernel='poly', degree=3)
model_poly.fit(X_train, y_train)
y_pred_poly = model_poly.predict(X_test)
print("Polynomial Kernel SVM Classification Report:")
print(classification_report(y_test, y_pred_poly))

# 3. SVM Model with RBF Kernel
model_rbf = SVC(kernel='rbf')
model_rbf.fit(X_train, y_train)
y_pred_rbf = model_rbf.predict(X_test)
print("RBF Kernel SVM Classification Report:")
print(classification_report(y_test, y_pred_rbf))
