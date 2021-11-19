from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, roc_auc_score
from sklearn.ensemble import RandomForestClassifier
import pandas as pd


features = ["acousticness", "danceability", "duration_ms", "energy", "instrumentalness",
            "liveness", "speechiness", "tempo", "valence"]
df = pd.read_csv("SpotifyFeatures.csv")
training = df.sample(frac=0.8, random_state=420)
X_train = training[features]
y_train = training['popularity']
X_test = df.drop(training.index)[features]
X_train, X_valid, y_train, y_valid = train_test_split(X_train, y_train, test_size=0.2, random_state=420)
# LR_Model = LogisticRegression()
# LR_Model.fit(X_train, y_train)
# LR_Predict = LR_Model.predict(X_valid)
# LR_Accuracy = accuracy_score(y_valid, LR_Predict)
# print("Accuracy: " + str(LR_Accuracy))
#
# LR_AUC = roc_auc_score(y_valid, LR_Predict, multi_class='ovr')
# print("AUC: " + str(LR_AUC))

RFC_Model = RandomForestClassifier()
RFC_Model.fit(X_train, y_train)
RFC_Predict = RFC_Model.predict(X_valid)
RFC_Accuracy = accuracy_score(y_valid, RFC_Predict)
print("Accuracy: " + str(RFC_Accuracy))

# RFC_AUC = roc_auc_score(y_valid, RFC_Predict)
# print("AUC: " + str(RFC_AUC))
