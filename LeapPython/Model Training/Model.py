import pickle
import pickle_compat as pkl
import joblib
import numpy as np
from PyQt5.QtWidgets import QFileDialog, QMessageBox,QTableWidgetItem
from PyQt5 import QtWidgets
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import minmax_scale, LabelEncoder,StandardScaler
from sklearn.tree import DecisionTreeClassifier
import seaborn as sn
from tasarimLeap import Ui_MainWindow
import sys
import pandas as pd




class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setupUi(self)
        self.confision=[]
        self.tahmin=0
        self.dosyaAdi = ""
        self.hsVeriSetiBoyutu.valueChanged.connect(self.hs_valueChanged)
        self.btnModelEgit.clicked.connect(self.model_Egit)
        self.btnConfusion.clicked.connect(self.confusionMatrix)
    def hs_valueChanged(self):
        val = "% " + str(self.hsVeriSetiBoyutu.value())
        self.lblBoyut.setText(val)
    def confusionMatrix(self):
        df_cm = pd.DataFrame(self.confision, index=[i for i in "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"],
                             columns=[i for i in "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"])
        plt.figure(figsize=(10, 7))
        sn.heatmap(df_cm, annot=True)
        plt.show()
    def readData(self,dosyaAdi):
        dsLeft = pd.read_csv("../DataSet/lefthand.csv", sep='|', header=None, encoding='latin-1')
        dsRight = pd.read_csv("../DataSet/righthand.csv", sep='|', header=None, encoding='latin-1')
        dsY = pd.read_csv("../DataSet/datasetY.csv", encoding='latin-1')
        print(dsLeft.shape)
        print(dsLeft)
        print(dsRight.shape)
        print(dsRight)


        datasetX = []
        for i in range(1, dsLeft.shape[0]):
            liste = []
            for j in range(0, dsLeft.shape[1]):
                liste.append(float(dsLeft[j][i]))
            for k in range(0, dsLeft.shape[1]):
                liste.append(float(dsRight[k][i]))
            datasetX.append(liste)

        dsY = np.array(dsY)
        labelDizi=[]
        for i in range(0,195):
            labelDizi.append(dsLeft[i][0])
        for i in range(0,195):
            labelDizi.append(dsRight[i][0])
        labels=labelDizi
        self.tblX.setRowCount(dsLeft.shape[0])
        self.tblX.setColumnCount(390)
        self.tblX.setHorizontalHeaderLabels(labels)
        self.tblY.setRowCount(dsY.shape[0])
        self.tblY.setColumnCount(1)
        labels2 = ['Class']
        self.tblY.setHorizontalHeaderLabels(labels2)
        for i, data in enumerate(datasetX):
            for j in range(0, len(data)):
                self.tblX.setItem(i, j, QTableWidgetItem(str(data[j])))
            self.tblY.setItem(i, 0, QTableWidgetItem(str(dsY[i])))
        return datasetX, dsY,labels,labels2
    def func_performansHesapla(self,cm):
        TN, TP, FP, FN = cm[0, 0], cm[1, 1], cm[0, 1], cm[1, 0]

        print("TP:", TP)
        print("TN:", TN)
        print("FP:", FP)
        print("FN:", FN)

        accuracy = (TP + TN) / (TP + FP + TN + FN) * 100
        sensitivity = TP / (TP + FN) * 100
        specificity = TN / (TN + FP) * 100

        print("Accuracy:", accuracy, " Sen:", sensitivity, " Spe", specificity)
        return accuracy,sensitivity,specificity
    def getIndex(self):
        index = self.cmbModel.currentIndex()
        return  index

    def model_Egit(self):
        if self.dosyaAdi == "":
            X, y,labels,labels2 = self.readData(self.dosyaAdi)
            sizeValue=float(self.hsVeriSetiBoyutu.value())
            sizeValue=sizeValue/100
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=sizeValue, random_state=42)
            X_train=np.array(X_train)
            y_train=np.array(y_train)
            X_test=np.array(X_test)
            y_test=np.array(y_test)
            column_number=X_train.shape[1]
            self.tblXTrain.setRowCount(X_train.shape[0])
            self.tblXTrain.setColumnCount(column_number)
            self.tblXTrain.setHorizontalHeaderLabels(labels)
            self.tblYTrain.setRowCount(y_train.shape[0])
            self.tblYTrain.setColumnCount(1)
            self.tblYTrain.setHorizontalHeaderLabels(labels2)
            self.tblXTest.setRowCount(X_test.shape[0])
            self.tblXTest.setColumnCount(column_number)
            self.tblXTest.setHorizontalHeaderLabels(labels)
            self.tblYTest.setRowCount(y_test.shape[0])
            self.tblYTest.setColumnCount(1)
            self.tblYTest.setHorizontalHeaderLabels(labels2)
            print("X:",X_train)
            print("Y:",y_train)

            for i, data in enumerate(X_train):
                for j in range(0, len(data)):
                    self.tblXTrain.setItem(i, j, QTableWidgetItem(str(data[j])))
                self.tblYTrain.setItem(i, 0, QTableWidgetItem(str(y_train[i])))
            for i, data in enumerate(X_test):
                for j in range(0, len(data)):
                    self.tblXTest.setItem(i, j, QTableWidgetItem(str(data[j])))
                self.tblYTest.setItem(i, 0, QTableWidgetItem(str(y_test[i])))
            cb = self.getIndex()
            model = RandomForestClassifier()
            if cb == 0:
                model =RandomForestClassifier()
            elif cb == 1:
                model = DecisionTreeClassifier()
            elif cb == 2:
                model = KNeighborsClassifier()
            model.fit(X_train, y_train)
            """ dosya = open('../RandomForest.joblib', 'wb')
            joblib.dump(model, dosya, protocol=2)"""
            predict = model.predict(X_test)

            print("Gerçekler")
            print(y_test)
            print("Tahminler")
            print(predict)
            dosya=open('../RandomForest.pkl','wb')
            pickle.dump(model,dosya)

            cm = confusion_matrix(y_test, predict)
            print(cm)
            basari = accuracy_score(y_test, predict)
            print("Başarı: ", basari)
            acc,sens,spe = self.func_performansHesapla(cm)

            """ w=open('../RandomForest.pkl','rb')
            rf = pickle.load(w)
            pickle.dump(rf, open("../RandomForest2.pkl", "wb"), protocol=2)"""
            self.lblACC.setText("Accuracy: {0}".format(basari))
            self.lblSen.setText("Sensitivity: {0}".format(sens))
            self.lblSpe.setText("Specificity: {0}".format(spe))
            self.confision=cm
            self.tahmin=predict

        else:
            QMessageBox.about(self,"Hata","Veri seti seçiniz!")
            QMessageBox.setStyleSheet(self,"")


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()