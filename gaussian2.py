# Q31. Gaussian Naive Bayes Classifier

from sklearn.naive_bayes import GaussianNB

X = [
    [50000, 700],
    [60000, 750],
    [30000, 600],
    [25000, 550]
]

y = [1, 1, 0, 0]

model = GaussianNB()
model.fit(X, y)

test_data = [[55000, 720]]

prediction = model.predict(test_data)

if prediction[0] == 1:
    print("Loan Approved")
else:
    print("Loan Rejected")