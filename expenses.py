# Form implementation generated from reading ui file 'expensis.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView, QAbstractItemView, QMessageBox,QWidget
from PyQt6.QtGui import QFont,QIcon
from PyQt6.QtCore import Qt, QSize, QRect, QPoint, QEvent

from Textslider import Slider, count, text,txt

# MESSAGE


from connection import databasename
import sqlite3

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 700)
        MainWindow.setWindowIcon(QIcon('logo/logo.jpeg'))
        self.closethis_page=MainWindow
        
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 0, 1311, 91))
        self.frame.setMouseTracking(False)
        self.frame.setTabletTracking(False)
        self.frame.setStyleSheet("QFrame{\n"
"background-color:blue;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.frame.setLineWidth(10)
        self.frame.setMidLineWidth(10)
        self.frame.setObjectName("frame")
        self.label_slider = QtWidgets.QLabel(parent=self.frame)
        self.label_slider.setGeometry(QtCore.QRect(30, 30, 1311, 40))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        self.label_slider.setFont(font)
        self.label_slider.setStyleSheet("QLabel{\n"
"color:rgb(255, 255, 255)\n"
"}")
        self.label_slider.setObjectName("label_slider")
        self.frame_2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(20, 100, 1311, 61))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.frame_2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 1301, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.add_btn = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.add_btn.setStyleSheet("QPushButton{\n"
"background-color:blue;\n"
"color:white\n"
"\n"
"}")
        self.add_btn.setObjectName("add_btn")
        self.horizontalLayout_2.addWidget(self.add_btn)
        self.sale_btn = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.sale_btn.setFont(QFont("sanserif",18))
        self.sale_btn.setStyleSheet("QPushButton{\n"
"color:white;\n"
"background-color:blue;\n"
"\n"
"}")
        self.sale_btn.setObjectName("sale_btn")
        self.horizontalLayout_2.addWidget(self.sale_btn)
        self.users_btn = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.users_btn.setFont(QFont("sanserif",18))
        self.users_btn.setStyleSheet("QPushButton{\n"
"color:white;\n"
"background-color:blue;\n"
"\n"
"}")
        self.users_btn.setObjectName("users_btn")
        self.horizontalLayout_2.addWidget(self.users_btn)
        self.customer_btn = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.customer_btn.setFont(QFont("sanserif",18))
        self.customer_btn.setStyleSheet("QPushButton{\n"
"color:white;\n"
"background-color:blue;\n"
"\n"
"}")
        self.customer_btn.setObjectName("customer_btn")
        self.horizontalLayout_2.addWidget(self.customer_btn)
        self.workers_btn = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.workers_btn.setFont(QFont("sanserif",18))
        self.workers_btn.setStyleSheet("QPushButton{\n"
"color:white;\n"
"background-color:blue;\n"
"\n"
"}")
        self.workers_btn.setObjectName("workers_btn")
        self.horizontalLayout_2.addWidget(self.workers_btn)
        self.expensive_btn = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.expensive_btn.setFont(QFont("sanserif",18))
        self.expensive_btn.setStyleSheet("QPushButton{\n"
"color:white;\n"
"background-color:blue;\n"
"\n"
"}")
        self.expensive_btn.setObjectName("expensive_btn")
        self.horizontalLayout_2.addWidget(self.expensive_btn)
        self.riders_btn = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.riders_btn.setFont(QFont("sanserif",18))
        self.riders_btn.setStyleSheet("QPushButton{\n"
"color:white;\n"
"background-color:blue;\n"
"\n"
"}")
        self.riders_btn.setObjectName("riders_btn")
        self.horizontalLayout_2.addWidget(self.riders_btn)
        self.calculator_btn = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.calculator_btn.setFont(QFont("sanserif",18))
        self.calculator_btn.setStyleSheet("QPushButton{\n"
"color:white;\n"
"background-color:blue;\n"
"\n"
"}")
        self.calculator_btn.setObjectName("calculator_btn")
        self.horizontalLayout_2.addWidget(self.calculator_btn)
        self.frame_3 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(30, 170, 371, 301))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(parent=self.frame_3)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(0, 10, 361, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.lineEdit_purpose = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_purpose.setFont(font)
        self.lineEdit_purpose.setObjectName("lineEdit_purpose")
        self.horizontalLayout_4.addWidget(self.lineEdit_purpose)
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.frame_3)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 240, 361, 41))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.save_btn = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.save_btn.setFont(QFont("sanserif",18))
        self.save_btn.setStyleSheet("QPushButton{\n"
"background-color:blue;\n"
"color:white;\n"
"}")
        self.save_btn.setObjectName("save_btn")
        self.verticalLayout.addWidget(self.save_btn)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(parent=self.frame_3)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(0, 60, 361, 41))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.lineEdit_from = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_from.setFont(font)
        self.lineEdit_from.setObjectName("lineEdit_from")
        self.horizontalLayout_5.addWidget(self.lineEdit_from)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(parent=self.frame_3)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(0, 110, 361, 41))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.lineEdit_to = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_to.setFont(font)
        self.lineEdit_to.setObjectName("lineEdit_to")
        self.horizontalLayout_6.addWidget(self.lineEdit_to)
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(parent=self.frame_3)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(0, 160, 361, 41))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_6 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.lineEdit_amount = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_amount.setFont(font)
        self.lineEdit_amount.setObjectName("lineEdit_amount")
        self.horizontalLayout_7.addWidget(self.lineEdit_amount)
        self.frame_table = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_table.setGeometry(QtCore.QRect(439, 220, 891, 351))
        self.frame_table.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_table.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_table.setObjectName("frame_table")
        self.frame_4 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(610, 170, 481, 61))
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayoutWidget_8 = QtWidgets.QWidget(parent=self.frame_4)
        self.horizontalLayoutWidget_8.setGeometry(QtCore.QRect(0, 0, 481, 41))
        self.horizontalLayoutWidget_8.setObjectName("horizontalLayoutWidget_8")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.lineEdit_search = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget_8)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_search.setFont(font)
        self.lineEdit_search.setObjectName("lineEdit_search")
        self.horizontalLayout_9.addWidget(self.lineEdit_search)
        self.search_btn = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_8)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.search_btn.setFont(QFont("sanserif",18))
        self.search_btn.setStyleSheet("QPushButton{\n"
"background-color:blue;\n"
"color:white;\n"
"}")
        self.search_btn.setObjectName("search_btn")
        self.horizontalLayout_9.addWidget(self.search_btn)
        self.frame_5 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(600, 580, 311, 31))
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.clear_table_btn = QtWidgets.QPushButton(parent=self.frame_5)
        self.clear_table_btn.setGeometry(QtCore.QRect(10, 0, 291, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.clear_table_btn.setFont(QFont("sanserif",18))
        self.clear_table_btn.setStyleSheet("QPushButton{\n"
"background-color:blue;\n"
"color:white\n"
"}")
        self.clear_table_btn.setObjectName("clear_table_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.creat_table()
        self.slider()
        
        self.add_btn.clicked.connect(self.openadditem)
        self.workers_btn.clicked.connect(self.openworkerspages)
        
        self.customer_btn.clicked.connect(self.opencustomaerspages)
        
        self.sale_btn.clicked.connect(self.opensalespages)
        
        self.riders_btn.clicked.connect(self.openriderpage)
        self.calculator_btn.clicked.connect(self.opencalculate)
        
        self.users_btn.clicked.connect(self.opencsv)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Add Item Window"))
        self.label_slider.setText(_translate("MainWindow", "TextLabel"))
        self.add_btn.setText(_translate("MainWindow", "Add Item"))
        self.add_btn.setFont(QFont("sanserif",18))
        self.sale_btn.setText(_translate("MainWindow", "Sales"))
        self.users_btn.setText(_translate("MainWindow", "CSV"))
        self.customer_btn.setText(_translate("MainWindow", "Customers"))
        self.workers_btn.setText(_translate("MainWindow", "Workers"))
        self.expensive_btn.setText(_translate("MainWindow", "Expenses"))
        self.riders_btn.setText(_translate("MainWindow", "Riders"))
        self.calculator_btn.setText(_translate("MainWindow", "Calculator"))
        self.label_3.setText(_translate("MainWindow", "Purpose"))
        self.save_btn.setText(_translate("MainWindow", "Save"))
        self.label_4.setText(_translate("MainWindow", "From "))
        self.label_5.setText(_translate("MainWindow", "To     "))
        self.label_6.setText(_translate("MainWindow", "Amount"))
        self.search_btn.setText(_translate("MainWindow", "Search"))
        self.clear_table_btn.setText(_translate("MainWindow", "Clear Table"))
        
        self.save_btn.clicked.connect(self.add_data)


    def creat_table(self):
            
            self.table=QTableWidget(self.frame_table)
            
            self.table.setColumnCount(5)
           
            self.table.resize(891, 351)
            self.table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
            self.table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
            self.table.setShowGrid(False)
            self.table.setWordWrap(True)
            self.table.setCornerButtonEnabled(False)
            self.table.setColumnWidth(0, 100)
            self.table.setAlternatingRowColors(True)
            self.table.verticalHeader().setVisible(False)
            self.table.horizontalHeader().setVisible(True)
            self.table.horizontalHeader().setStretchLastSection(True)
            self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
            self.table.setSortingEnabled(True)
            self.table.horizontalHeader().setStyleSheet("QHeaderView::section{background-color:black; color:white; font-size:15px}")
            self.table.setStyleSheet(" color:black")
            self.table.move(0,0)
            self.table.setHorizontalHeaderLabels(['ID','From','To','Purpose','Amount'])
            
            self.fetch_data()
            
    def fetch_data(self):
            conn = sqlite3.connect(databasename)
            cur = conn.cursor()
            cur.execute("SELECT * FROM expenses")
            rows = cur.fetchall()
            conn.close()
        #     return rows
        #     create tabel
            self.table.setRowCount(len(rows))
            for row, form in enumerate(rows):
                    self.table.setItem(row, 0, QTableWidgetItem(str(form[0])))
                    self.table.setItem(row, 1, QTableWidgetItem(str(form[1])))
                    self.table.setItem(row, 2, QTableWidgetItem(str(form[2])))
                    self.table.setItem(row, 3, QTableWidgetItem(str(form[3])))
                    self.table.setItem(row, 4, QTableWidgetItem("₵" +str(form[4])))
                   
                   
                    
    def add_data(self):
            
            
            conn=sqlite3.connect(databasename)
            cur=conn.cursor()
            values = (
                    self.lineEdit_from.text(),
                    self.lineEdit_to.text(),
                    self.lineEdit_purpose.text(),
                    float(self.lineEdit_amount.text())
               
            )
            cur.execute("INSERT INTO expenses(giver,reciver,purpose,amount) VALUES (?,?,?,?)",values)
            conn.commit()
            conn.close()
            self.clear_data()
            self.fetch_data()
            
    def clear_data(self):
            self.lineEdit_from.clear,
            self.lineEdit_to.clear,
            self.lineEdit_purpose.clear,
            self.lineEdit_amount.clear
            
            
            
            
    def slider(self):
            global text,count
            Slider(self.label_slider)   
                
# page opening configuration

    def openworkerspages(self):
            from workers import Ui_MainWindow
            self.wworkerpage = QtWidgets.QMainWindow()
            self.openworker = Ui_MainWindow()
            self.openworker.setupUi(self.wworkerpage)
            self.closethis_page.close()
            self.wworkerpage.show()
            
            
    def opencustomaerspages(self):
            from customers import Ui_MainWindow
            
            self.customerpage = QtWidgets.QMainWindow()
            self.cuspage = Ui_MainWindow()
            self.cuspage.setupUi(self.customerpage)
            self.closethis_page.close()
            self.customerpage.show()
            
    def openriderpage(self):
            from riders import Ui_MainWindow
            
            self.riderpage = QtWidgets.QMainWindow()
            self.rider_p = Ui_MainWindow()
            self.rider_p.setupUi(self.riderpage)
            self.closethis_page.close()
            self.riderpage.show()
            
    def opensalespages(self):
            from sales import Ui_MainWindow
            
            self.salespage = QtWidgets.QMainWindow()
            self.salesopen = Ui_MainWindow()
            self.salesopen.setupUi(self.salespage)
            self.closethis_page.close()
            self.salespage.show()
            
            
            
    def openadditem(self):
            from additemui import Ui_MainWindow
            
            self.addpage = QtWidgets.QMainWindow()
            self.additem = Ui_MainWindow()
            self.additem.setupUi(self.addpage)
            self.closethis_page.close()
            self.addpage.show()
            
            

    def opencalculate(self):
            from calculator import Ui_Dialog
            
            self.calculate = QtWidgets.QDialog()
            self.calculate_c = Ui_Dialog()
            self.calculate_c.setupUi(self.calculate)
        #     self.addwindowpage.close()
            self.calculate.show()
            

    def opencsv(self):
            from csvpages import Ui_Dialog
            
            self.csvfile = QtWidgets.QDialog()
            self.csfpage = Ui_Dialog()
            self.csfpage.setupUi(self.csvfile)
        #     self.addwindowpage.close()
            self.csvfile.show()            



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
