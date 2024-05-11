
'''
Function: train_model

Description: This function takes 3 arguments as input-df(pandas dataframe),target field(click) & input field(user info like age,gender,his_app_size etc).
Then it uses scikitlearn ml package and train a model to predict r forcast ctr for ad bassed on user data.

Developer: Team Deadline Doers

Date: 10 May,2024
'''

# import external libs

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score, roc_auc_score

def train_model(df,target_col,inp_col):
    df[target_col]=df[target_col].astype(int)

    X = df[[inp_col]]
    y = df[target_col]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    conf_matrix = confusion_matrix(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    roc_auc = roc_auc_score(y_test, y_pred)

    print(f"Accuracy: {accuracy:.4f}")
    print("\nConfusion Matrix:")
    print(conf_matrix)
    print(f"\nPrecision: {precision:.4f}")
    print(f"Recall: {recall:.4f}")
    print(f"F1 Score: {f1:.4f}")
    print(f"\nROC-AUC Score: {roc_auc:.4f}")