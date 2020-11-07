# Project based learning



from pyqt_edit import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, Qt, QtWidgets
import sys
import math
import graph_plot


class mainwinn(QMainWindow,Ui_MainWindow ):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.minimize.clicked.connect(lambda x: self.showMinimized())
        self.cLose.clicked.connect(self.Maxim_mini)
        self.tile_bar.mouseMoveEvent = self.moveWindow
        self.next.clicked.connect(self.page2)
        self.maximize.clicked.connect(lambda x : self.close())
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.comboBox_pg2.addItem("0 gm")
        self.comboBox_pg2.addItem("100 gm")
        self.comboBox_pg2.addItem("200 gm")
        self.comboBox_pg2.addItem("500 gm")
        self.frame_7.setVisible(False)
        self.frame_9.setVisible(False)
        self.frame_10.setVisible(False)
        self.time_taken.setVisible(False)
        self.label_7.setVisible(False)
        self.frame_24.setVisible(False)
        self.frame_25.setVisible(False)
        self.frame_26.setVisible(False)
        self.comboBox_pg2.currentIndexChanged.connect(self.CurrentText)
        self.pushButton.setEnabled(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.frame_30.setVisible(False)
        self.frame_36.setVisible(False)
        self.frame_38.setVisible(False)
        self.pushButton_2.clicked.connect(self.graph)
        self.onlyfloat = QtGui.QDoubleValidator()
        self.lineEdit.setValidator(self.onlyfloat)
        self.lineEdit_2.setValidator(self.onlyfloat)
        self.lineEdit_3.setValidator(self.onlyfloat)
        self.lineEdit_4.setValidator(self.onlyfloat)
        self.lineEdit_5.setValidator(self.onlyfloat)
        self.lineEdit_6.setValidator(self.onlyfloat)

    def Maxim_mini(self):
        global GLOBAL_i
        if GLOBAL_i == 1:
            self.showMaximized()
            self.frame.setContentsMargins(0,0,0,0)
            GLOBAL_i = 0

        else :
            self.showNormal()

            GLOBAL_i = 1

    def moveWindow(self, event):
        if GLOBAL_i == 0:
            self.showNormal()

        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.pos() - self.dragPos )

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()


    def page2(self):
        global nexty
        if nexty == 1:
            self.next.setEnabled(False)
            self.pg1.setMaximumSize(QtCore.QSize(0, 16777215))
            self.pg2.setMaximumSize(QtCore.QSize(16777215, 16777215))
            nexty += 1
            return nexty

        if nexty == 2:
            self.pg2.setMaximumSize(QtCore.QSize(0, 16777215))
            self.pg3.setMaximumSize(QtCore.QSize(16777215, 16777215))

    def CurrentText(self):
        vvg = str(self.comboBox_pg2.currentText())
        if vvg == "0 gm" :
            self.spring01(0)
        if vvg == "100 gm":
            self.spring01(100)

        if vvg == "200 gm":
            self.spring01(200)

        if vvg == "500 gm":
            self.spring01(500)

    def spring01(self, mass):
        if mass == 100 :
            self.spring.setMaximumSize(QtCore.QSize(0, 16777215))
            self.spring_100.setMaximumSize(QtCore.QSize(16777215, 16777215))
            self.spring_200.setMaximumSize(QtCore.QSize(0, 16777215))
            self.spring_500.setMaximumSize(QtCore.QSize(0, 16777215))

        if mass == 200 :
            self.spring.setMaximumSize(QtCore.QSize(0, 16777215))
            self.spring_100.setMaximumSize(QtCore.QSize(0, 16777215))
            self.spring_200.setMaximumSize(QtCore.QSize(16777215, 16777215))
            self.spring_500.setMaximumSize(QtCore.QSize(0, 16777215))

        if mass == 500 :
            self.spring.setMaximumSize(QtCore.QSize(0, 16777215))
            self.spring_100.setMaximumSize(QtCore.QSize(0, 16777215))
            self.spring_200.setMaximumSize(QtCore.QSize(0, 16777215))
            self.spring_500.setMaximumSize(QtCore.QSize(16777215, 16777215))

        if mass == 0 :
            self.spring.setMaximumSize(QtCore.QSize(16777215, 16777215))
            self.spring_100.setMaximumSize(QtCore.QSize(0, 16777215))
            self.spring_200.setMaximumSize(QtCore.QSize(0, 16777215))
            self.spring_500.setMaximumSize(QtCore.QSize(0, 16777215))

        self.frame_7.setVisible(True)
        self.frame_9.setVisible(True)
        self.frame_10.setVisible(True)
        self.lineEdit_2.editingFinished.connect(lambda :self.timetkn(mass))

    def rem(self, mass):
        self.frame_25.setVisible(True)
        self.frame_26.setVisible(True)
        self.lineEdit_4.editingFinished.connect(lambda :self.rem2(mass))

    def rem2(self, mass):
        self.frame_30.setVisible(True)
        self.pushButton.setEnabled(True)
        self.lineEdit_5.editingFinished.connect(lambda : self.record(mass))

    def record(self, mass):
        class properties:
            def __init__(self,length, mass, static, konstant, time, frequency, natural):
                self.length = length
                self.mass= mass
                self.static = static
                self.konstant = konstant
                self.time = time
                self.frequency = frequency
                self.natural = natural
        self.lineEdit.setReadOnly(True)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_4.setReadOnly(True)
        if mass == 100:
            lenth = 0.193
        if mass == 200:
            lenth = 0.198
        if mass == 500:
            lenth = 0.215
        m = mass * 0.001
        delta = lenth - 0.118
        try:
            K = float(self.lineEdit.text())
            t1 = float(self.lineEdit_3.text())
            freq = float (self.lineEdit_4.text())
            nat = float(self.lineEdit_5.text())
            props1 = properties(lenth, m, delta, K, t1, freq, nat)
        except ValueError:
            print("___")
        except UnboundLocalError:
            print("////////")
        self.pushButton.clicked.connect(lambda : self.table(props1))

    def timetkn(self,m):
        global num1
        K  = self.lineEdit.text()
        osc = self.lineEdit_2.text()
        try:
            print(int(osc))
            wn = math.sqrt(float(K) / (m*0.001 + 0.005))
            num = ((2 * 3.142) / wn)*int(osc)
            num1 = round(num, 2)
            self.comboBox_pg2.setEnabled(False)
            text = "Time taken for " + osc + " oscillations = " + str(num1) + " seconds"
            self.time_taken.setText(text)
            self.time_taken.setVisible(True)
            self.label_7.setVisible(True)
            self.frame_24.setVisible(True)
            self.lineEdit_3.editingFinished.connect(lambda :self.rem(m))
        except ValueError :
            print("....")
        except ZeroDivisionError:
            print(".......")

    def table(self, val):
        val2 = []
        self.next.setEnabled(True)
        val2.append(val)
        self.comboBox_pg2.setEnabled(True)
        self.lineEdit.setReadOnly(False)
        self.lineEdit_2.setReadOnly(False)
        self.lineEdit_3.setReadOnly(False)
        self.lineEdit_4.setReadOnly(False)
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        y = len(val2)
        for x in range(0, y):
            a = round(val2[x].static, 2)
            self.tableWidget.setItem(x, 0, QTableWidgetItem(str(val2[x].length)))
            self.tableWidget.setItem(x, 1, QTableWidgetItem(str(val2[x].mass)))
            self.tableWidget.setItem(x, 2, QTableWidgetItem(str(a)))
            self.tableWidget.setItem(x, 3, QTableWidgetItem(str(val2[x].konstant)))
            self.tableWidget.setItem(x, 4, QTableWidgetItem(str(val2[x].time)))
            self.tableWidget.setItem(x, 5, QTableWidgetItem(str(val2[x].frequency)))
            self.tableWidget.setItem(x, 6, QTableWidgetItem(str(val2[x].natural)))
        self.lineEdit_6.editingFinished.connect(lambda: self.graph2(val2))


    def graph(self):
        self.frame_38.setVisible(True)
        self.frame_36.setVisible(True)
        self.comboBox.addItem("1")
        self.comboBox.addItem("2")
        self.comboBox.addItem("3")
        self.comboBox.addItem("4")
        self.comboBox.addItem("5")

    def graph2(self, val2):
        self.comboBox.setEnabled(False)
        self.pushButton_3.clicked.connect(lambda :self.graph3(val2))

    def graph3(self, val2):
        number = int(self.comboBox.currentText())
        damping_ratio = self.lineEdit_6.text()
        graph_plot.main(val2, number,float(damping_ratio))


nexty = 1
GLOBAL_i = 1
app = QtWidgets.QApplication(sys.argv)
window = mainwinn()
window.show()
app.exec()
