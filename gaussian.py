# Q8. Gaussian Naive Bayes Classifier

from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

X, y = make_blobs(
    n_samples=200,
    centers=3,
    n_features=2,
    cluster_std=1.5,
    random_state=42
)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = GaussianNB()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)

new_data = [
    [-2, 5],
    [0, 0],
    [6, -0.3]
]

prediction = model.predict(new_data)

print("Prediction:", prediction)