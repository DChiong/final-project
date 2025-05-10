# train_model.py
import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

df = pd.read_csv('student_exam_data_new.csv')
df.columns = ['study_hours', 'exam_score', 'pass_fail']

X = df[['study_hours', 'exam_score']]
y = df['pass_fail']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X, y)


# Step 6: Make predictions
y_pred = model.predict(X_test)


# Step 7: Evaluate the model
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

joblib.dump(model, 'model.pkl')
