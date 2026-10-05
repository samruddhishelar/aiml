# Q29. Analyze SVM Classifier Performance

from sklearn import svm
from sklearn.metrics import accuracy_score

X = [
    [1, 2],
    [2, 3],
    [3, 1],
    [7, 6],
    [8, 7],
    [9, 5]
]

y = [0, 0, 0, 1, 1, 1]

X_test = [
    [2, 2],
    [8, 6],
    [3, 2],
    [7, 7]
]

y_test = [0, 0, 0, 1]

model = svm.SVC(kernel='linear')
model.fit(X, y)

prediction = model.predict(X_test)

accuracy = accuracy_score(y_test, prediction)

print("Linear SVM Predictions:", prediction)
print("Linear SVM Accuracy:", accuracy)