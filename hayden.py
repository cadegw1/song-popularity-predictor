from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import make_scorer, accuracy_score, roc_auc_score 
features = ['length', 'danceability', 'acousticness', 'energy', 'instrumentalness', 'liveness', 'speechiness', 'tempo']
training = df.sample(frac = 0.8)
X_train = training[features]
y_train = training['popularity']
X_test = df.drop(training.index)[features]
X_train, X_valid, y_train, y_valid = train_test_split(X_train, y_train, test_size = 0.2)
LR_Model = LogisticRegression()
LR_Model.fit(X_train, y_train)
LR_Predict = LR_Model.predict(X_valid)
LR_Accuracy = accuracy_score(y_valid, LR_Predict)
print("Accuracy: " + str(LR_Accuracy))

LR_AUC = roc_auc_score(y_valid, LR_Predict) 
print("AUC: " + str(LR_AUC))
