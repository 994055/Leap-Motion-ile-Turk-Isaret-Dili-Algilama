
import pandas as pd
import numpy as np
import sklearn
dsLeft = pd.read_csv("../DataSet/lefthand.csv", sep='|')
dsRight = pd.read_csv("../DataSet/righthand.csv", sep='|')
dsY = pd.read_csv("../DataSet/datasetY.csv")
datasetX = []
for i in range(1, dsLeft.shape[0]):
    liste = []
    for j in range(0, dsLeft.shape[1]):
        liste.append(dsLeft[j][i])
    for k in range(0, dsLeft.shape[1]):
        liste.append(dsRight[k][i])
    datasetX.append(liste)

dsY = np.array(dsY)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=sizeValue, random_state=42)
X_train=np.array(X_train)
y_train=np.array(y_train)
X_test=np.array(X_test)
y_test=np.array(y_test)
print("X:", X_train)
print("Y:", y_train)
model =RandomForestClassifier(n_estimators=40)
model.fit(X_train, y_train)
predict = model.predict(X_test)
print("Gerçekler")
print(y_test)
print("Tahminler")
print(predict)

cm = confusion_matrix(y_test, predict)
print(cm)
basari = accuracy_score(y_test, predict)
print("Başarı: ", basari)
output = open('../RandomForest.pkl', 'wb')
pickle.dump(model, output)