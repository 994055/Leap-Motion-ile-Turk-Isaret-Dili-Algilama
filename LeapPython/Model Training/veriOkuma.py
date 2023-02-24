import pickle
import seaborn as sn
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split


dsLeft = pd.read_csv("../DataSet/lefthand.csv", sep='|', header=None, encoding='latin-1')
dsRight = pd.read_csv("../DataSet/righthand.csv", sep='|', header=None, encoding='latin-1')
dsY = pd.read_csv("../DataSet/datasetY.csv", encoding='latin-1')

dfLeft = np.array(dsLeft.values)
dfRight = np.array(dsRight.values)
print(dsLeft.shape)
print(dsLeft)
print(dsRight.shape)
print(dsRight)
print(dsLeft[1][1]+' '+dsRight[1][1])

datasetX=[]
for i in range(1,dsLeft.shape[0]):
    liste=[]
    for j in range(0,dsLeft.shape[1]):
        liste.append(dsLeft[j][i])
    for k in range(0,dsLeft.shape[1]):
        liste.append(dsRight[k][i])
    datasetX.append(liste)

dsY=np.array(dsY)
X_train,X_test,y_train,y_test = train_test_split(datasetX,dsY,test_size=0.3,random_state=43,shuffle=True)
print(X_train)
model = RandomForestClassifier()
print("y train",y_train)
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
df_cm = pd.DataFrame(cm, index = [i for i in "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"],
                  columns = [i for i in "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"])
plt.figure(figsize = (10,7))
sn.heatmap(df_cm, annot=True)
plt.show()
file_name = "RandomForest.pkl"
pickle.dump(model, open(file_name, "wb"))

