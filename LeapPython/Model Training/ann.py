import numpy as np
import pandas as pd
import seaborn as sns

from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.utils.version_utils import callbacks
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, MinMaxScaler,StandardScaler

dsLeft = pd.read_csv("../DataSet/lefthand.csv", sep='|', header=None, encoding='latin-1')
dsRight = pd.read_csv("../DataSet/righthand.csv", sep='|', header=None, encoding='latin-1')
dsY = pd.read_csv("../DataSet/datasetY.csv", encoding='latin-1')
datasetX = []
liste=[]

for i in range(1, dsLeft.shape[0]):
    liste = []
    for j in range(0, dsLeft.shape[1]):
        liste.append(float(dsLeft[j][i]))
    for k in range(0, dsLeft.shape[1]):
        liste.append(float(dsRight[k][i]))
    datasetX.append(liste)
scalr=StandardScaler(copy=True,with_mean=True,with_std=True)
datasetX=scalr.fit_transform(datasetX)
dsY = np.array(dsY)
X_train, X_test, y_train, y_test = train_test_split(datasetX, dsY, test_size=0.25, random_state=42)
X_train = np.array(X_train)
y_train = np.array(y_train)
X_test = np.array(X_test)
y_test = np.array(y_test)
print(X_train)
print(X_train.shape)
ann = Sequential()
#Gizli(hidden) katmanlar oluşturuldu.
ann.add(Dense(512, activation='relu', input_dim=390))
ann.add(Dropout(0.5))
ann.add(Dense(500, activation='relu'))
ann.add(Dense(500, activation='relu'))
ann.add(Dense(500, activation='relu'))
ann.add(Dense(500, activation='relu'))
ann.add(Dense(500, activation='relu'))
ann.add(Dropout(0.5))
ann.add(Dense(500, activation='relu'))
ann.add(Dense(1, activation='sigmoid'))
#Çıktı(output) katmanı oluşturuldu.
ann.add(Dense(units=1,activation="sigmoid",kernel_initializer='normal'))
#Yapay sinir ağı modelimiz derlendi.
ann.compile(optimizer="rmsprop",loss="mean_squared_error",metrics=['accuracy'])
#Erken durdurma yöntemi ile başarı değeri en yüksek olan epoch aşamasında model eğitimi durdurulacak.
earlystopping = callbacks.EarlyStopping(monitor='val_loss',
                                        mode='min',
                                        verbose=1,
                                        patience=20)
#Modelin eğitim aşaması gerçekleştirildi.
history = ann.fit(X_train, y_train,validation_data=(X_test,y_test), batch_size = 60, epochs = 500, callbacks =[earlystopping])
y_pred = ann.predict(X_test)
y_pred = (y_pred > 0.5)
ann_cm = confusion_matrix(y_test, y_pred)
ann_acc = round(accuracy_score(y_pred,y_test) * 100, 2)
print(ann_cm)
print(ann_acc,'%')
print(classification_report(y_pred,y_test))