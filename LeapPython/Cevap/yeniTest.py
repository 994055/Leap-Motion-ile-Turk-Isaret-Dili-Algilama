import os

import numpy as np
import pandas as pd
import pickle
from playsound import playsound
from gtts import gTTS

filename=("../Models/RandomForest.pkl")
loaded_model = pickle.load(open(filename, 'rb'))
datasetX = np.load("../dataX.npy")
datasetX=np.array(datasetX)
print(datasetX.shape)
result =loaded_model.predict(datasetX)
print(result)
metin=""
for i in range(1,len(result)):
    if result[i] == 1:
        metin += "a"
    elif result[i] == 2:
        metin += "b"
    elif result[i] == 3:
        metin += "c"
    elif result[i] == 4:
        metin += "ç"
    elif result[i] == 5:
        metin += "d"
    elif result[i] == 6:
        metin += "e"
    elif result[i] == 7:
        metin += "f"
    elif result[i] == 8:
        metin += "g"
    elif result[i] == 9:
        metin += "ğ"
    elif result[i] == 10:
        metin += "h"
    elif result[i] == 11:
        metin += "ı"
    elif result[i] == 12:
        metin += "i"
    elif result[i] == 13:
        metin += "j"
    elif result[i] == 14:
        metin += "k"
    elif result[i] == 15:
        metin += "l"
    elif result[i] == 16:
        metin += "m"
    elif result[i] == 17:
        metin += "n"
    elif result[i] == 18:
        metin += "o"
    elif result[i] == 19:
        metin += "ö"
    elif result[i] == 20:
        metin += "p"
    elif result[i] == 21:
        metin += "r"
    elif result[i] == 22:
        metin += "s"
    elif result[i] == 23:
        metin += "ş"
    elif result[i] == 24:
        metin += "t"
    elif result[i] == 25:
        metin += "u"
    elif result[i] == 26:
        metin += "ü"
    elif result[i] == 27:
        metin += "v"
    elif result[i] == 28:
        metin += "y"
    elif result[i] == 29:
        metin += "z"
    elif result[i] == 30:
        metin += " "
print(metin)
tts = gTTS(text=metin,lang="tr")
file="answer.mp3"
tts.save(file)
playsound(file)
os.remove(file)

