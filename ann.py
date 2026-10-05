# Q22. ANN for Linear Regression

from sklearn.neural_network import MLPRegressor
import matplotlib.pyplot as plt

X = [
    [1],
    [2],
    [3],
    [4],
    [5]
]

y = [20, 30, 40, 50, 60]

model = MLPRegressor(
    hidden_layer_sizes=(5,),
    max_iter=5000,
    random_state=42
)

model.fit(X, y)

y_pred = model.predict(X)

new_student = [[6]]
prediction = model.predict(new_student)

print("Predicted Marks for 6 Hours:", round(prediction[0], 2))

plt.scatter(X, y, label="Actual Data")
plt.plot(X, y_pred, label="ANN Prediction")

plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("ANN Linear Regression")
plt.legend()
plt.show()