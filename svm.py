# Q10. Support Vector Machine (SVM) on Iris Dataset

from sklearn.svm import SVC

X = [
    [5.1, 3.5, 1.4, 0.2],
    [4.9, 3.0, 1.4, 0.2],
    [4.7, 3.2, 1.3, 0.2],
    [4.6, 3.1, 1.5, 0.2],
    [5.0, 3.6, 1.4, 0.2],
    [7.0, 3.2, 4.7, 1.4],
    [6.4, 3.2, 4.5, 1.5],
    [6.9, 3.1, 4.9, 1.5],
    [6.3, 3.3, 6.0, 2.5],
    [5.8, 2.7, 5.1, 1.9]
]

y = [0, 0, 0, 0, 0, 1, 1, 1, 2, 2]

model = SVC(kernel='linear')

model.fit(X, y)

X_test = [
    [5.2, 3.4, 1.5, 0.2],
    [6.5, 3.0, 4.6, 1.5],
    [6.2, 3.0, 5.2, 2.0]
]

prediction = model.predict(X_test)

print("Predicted Classes:", prediction)

for p in prediction:
    if p == 0:
        print("Setosa")
    elif p == 1:
        print("Versicolor")
    else:
        print("Virginica")