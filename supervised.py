# Q30. Supervised vs Unsupervised Learning

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score

iris = load_iris()

X = iris.data
y = iris.target

# Supervised Learning

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("Supervised Learning")
print("-------------------")
print("Predictions:", y_pred)
print("Accuracy:", accuracy * 100, "%")

# Unsupervised Learning

kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

clusters = kmeans.fit_predict(X)

print("\nUnsupervised Learning")
print("---------------------")
print("Cluster Labels:", clusters)
print("Number of Clusters:", 3)