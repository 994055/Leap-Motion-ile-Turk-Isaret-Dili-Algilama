import os

import numpy as np
import pandas as pd
import pickle
from playsound import playsound
from gtts import gTTS

filename=("../Models/RandomForest.pkl")
loaded_model = pickle.load(open(filename, 'rb'))
dsLeft = pd.read_csv("../DataSet/leftdene.csv", sep='|', header=None, encoding='latin-1')
dsRight = pd.read_csv("../DataSet/rightdene.csv", sep='|', header=None, encoding='latin-1')



datasetX = []
for i in range(1, dsLeft.shape[0]):
     liste = []
     for j in range(0, dsLeft.shape[1]):
        liste.append(dsLeft[j][i])
     for k in range(0, dsLeft.shape[1]):
        liste.append(dsRight[k][i])
     datasetX.append(liste)

result =loaded_model.predict(datasetX)
print(result)
metin=""
for i in range(len(result)):
    if result[i]==2:
        metin+="b"
    elif result[i]==6:
        metin+="e"
    elif result[i]==19:
        metin+="ö"
print(metin)
tts = gTTS(text=metin,lang="tr")
file="answer.mp3"
tts.save(file)
playsound(file)
os.remove(file)

