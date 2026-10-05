# Q11. Non-Linear SVM using RBF Kernel

from sklearn.svm import SVC

X = [
    [1, 2],
    [2, 3],
    [5, 5]
]

y = [0, 0, 1]

model = SVC(kernel='rbf')
model.fit(X, y)

test_data = [[4, 4]]

prediction = model.predict(test_data)

print("Prediction:", prediction)

if prediction[0] == 0:
    print("Class 0")
else:
    print("Class 1")