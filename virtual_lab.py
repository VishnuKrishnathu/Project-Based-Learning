from PyQt5.QtWidgets import *
from pyqt_edit import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import math
import graph_plot
import sys
from class_name import *

class main_window(QMainWindow, Ui_MainWindow, properties):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.val2 = []
        self.minimize.clicked.connect(lambda x: self.showMinimized())
        self.cLose.clicked.connect(self.Maxim_mini)
        self.tile_bar.mouseMoveEvent = self.moveWindow
        self.next.clicked.connect(self.page2)
        self.maximize.clicked.connect(lambda x: self.close())
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        ################ comboBox Items ##################
        self.comboBox_pg2.addItem("0 gm")
        self.comboBox_pg2.addItem("100 gm")
        self.comboBox_pg2.addItem("200 gm")
        self.comboBox_pg2.addItem("500 gm")
        self.comboBox.addItem("1")
        self.comboBox.addItem("2")
        self.comboBox.addItem("3")
        self.comboBox.addItem("4")
        self.comboBox.addItem("5")
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.onlyfloat = QtGui.QDoubleValidator()
        self.lineEdit.setValidator(self.onlyfloat)
        self.lineEdit_2.setValidator(self.onlyfloat)
        self.lineEdit_3.setValidator(self.onlyfloat)
        self.lineEdit_4.setValidator(self.onlyfloat)
        self.lineEdit_5.setValidator(self.onlyfloat)
        self.lineEdit_6.setValidator(self.onlyfloat)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.lineEdit.textChanged.connect(self.record_lineEdit)
        self.comboBox_pg2.currentIndexChanged.connect(self.combobox_item)
        self.lineEdit_2.textChanged.connect(self.record_lineEdit2)
        self.lineEdit_3.textChanged.connect(self.record_lineEdit3)
        self.lineEdit_4.textChanged.connect(self.record_lineEdit4)
        self.lineEdit_5.textChanged.connect(self.record_lineEdit5)
        self.pushButton.clicked.connect(self.accept_func)
        self.pushButton_3.clicked.connect(self.plot_graph)

    def record_lineEdit(self):
        self.spring_constant = self.lineEdit.text()

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
            y = len(self.val2)
            for x in range(0, y):
                a = round(self.val2[x].static, 2)
                self.tableWidget.setItem(x, 0, QTableWidgetItem(str(self.val2[x].length)))
                self.tableWidget.setItem(x, 1, QTableWidgetItem(str(self.val2[x].mass)))
                self.tableWidget.setItem(x, 2, QTableWidgetItem(str(a)))
                self.tableWidget.setItem(x, 3, QTableWidgetItem(self.val2[x].konstant))
                self.tableWidget.setItem(x, 4, QTableWidgetItem(self.val2[x].time))
                self.tableWidget.setItem(x, 5, QTableWidgetItem(self.val2[x].frequency))
                self.tableWidget.setItem(x, 6, QTableWidgetItem(self.val2[x].natural))

    def combobox_item(self):
        self.selection = str(self.comboBox_pg2.currentText())
        if self.selection == "0 gm":
            self.spring01(0)
        if self.selection == "100 gm":
            self.spring01(100)

        if self.selection == "200 gm":
            self.spring01(200)

        if self.selection == "500 gm":
            self.spring01(500)

    def spring01(self, mass):
        if mass == 100:
            self.spring.setMaximumSize(QtCore.QSize(0, 16777215))
            self.spring_100.setMaximumSize(QtCore.QSize(16777215, 16777215))
            self.spring_200.setMaximumSize(QtCore.QSize(0, 16777215))
            self.spring_500.setMaximumSize(QtCore.QSize(0, 16777215))

        if mass == 200:
            self.spring.setMaximumSize(QtCore.QSize(0, 16777215))
            self.spring_100.setMaximumSize(QtCore.QSize(0, 16777215))
            self.spring_200.setMaximumSize(QtCore.QSize(16777215, 16777215))
            self.spring_500.setMaximumSize(QtCore.QSize(0, 16777215))

        if mass == 500:
            self.spring.setMaximumSize(QtCore.QSize(0, 16777215))
            self.spring_100.setMaximumSize(QtCore.QSize(0, 16777215))
            self.spring_200.setMaximumSize(QtCore.QSize(0, 16777215))
            self.spring_500.setMaximumSize(QtCore.QSize(16777215, 16777215))

        if mass == 0:
            self.spring.setMaximumSize(QtCore.QSize(16777215, 16777215))
            self.spring_100.setMaximumSize(QtCore.QSize(0, 16777215))
            self.spring_200.setMaximumSize(QtCore.QSize(0, 16777215))
            self.spring_500.setMaximumSize(QtCore.QSize(0, 16777215))
        self.mass_value = mass

    def record_lineEdit2(self):
        self.oscillations = self.lineEdit_2.text()
        try:
            print(int(self.oscillations))
            wn = math.sqrt(float(self.spring_constant) / (self.mass_value*0.001 + 0.005))
            num = ((2 * 3.142) / wn)*int(self.oscillations)
            num1 = round(num, 2)
            self.comboBox_pg2.setEnabled(False)
            text = "Time taken for " + self.oscillations + " oscillations = " + str(num1) + " seconds"
            self.time_taken.setText(text)
        except :
            pass

    def record_lineEdit3(self):
        self.time_period = self.lineEdit_3.text()

    def record_lineEdit4(self):
        self.frequency = self.lineEdit_4.text()

    def record_lineEdit5(self):
        try :
            self.natural_frequency = self.lineEdit_5.text()
            self.lineEdit.setReadOnly(True)
            self.lineEdit_2.setReadOnly(True)
            self.lineEdit_3.setReadOnly(True)
            self.lineEdit_4.setReadOnly(True)
            if self.mass_value == 100:
                lenth = 0.193
            if self.mass_value == 200:
                lenth = 0.198
            if self.mass_value == 500:
                lenth = 0.215
            m = self.mass_value * 0.001
            delta = lenth - 0.118
            self.value_storage = properties(lenth, m, delta, self.spring_constant, self.time_period, self.frequency, self.natural_frequency)
        except:
            pass
    def accept_func(self):
        self.next.setEnabled(True)
        self.val2.append(self.value_storage)
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

    def plot_graph(self):
        self.num = int(self.comboBox.currentText())
        self.zeta = float(self.lineEdit_6.text())
        graph_plot.main(self.val2, self.num, self.zeta)


nexty = 1
GLOBAL_i = 1
app = QApplication(sys.argv)
window = main_window()
window.show()
app.exec()
