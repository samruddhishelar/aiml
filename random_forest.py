# Q17. Random Forest Classifier

import pandas as pd
from sklearn.ensemble import RandomForestClassifier

dataset = {
    'Study_Hours': [2, 3, 4, 5, 6, 7, 1, 2, 5, 8],
    'Attendance': [60, 65, 70, 75, 80, 85, 55, 62, 78, 90],
    'Assignment_Score': [55, 60, 65, 70, 75, 80, 50, 58, 72, 85],
    'Result': [
        'Fail', 'Fail', 'Pass', 'Pass', 'Pass',
        'Pass', 'Fail', 'Fail', 'Pass', 'Pass'
    ]
}

df = pd.DataFrame(dataset)

X = df[
    ['Study_Hours', 'Attendance', 'Assignment_Score']
]

y = df['Result']

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

test_data = [[6, 82, 78]]

prediction = model.predict(test_data)

print("Test Data:", test_data)
print("Predicted Result:", prediction[0])