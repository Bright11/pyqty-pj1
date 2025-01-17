# Form implementation generated from reading ui file 'customers.ui'
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
from query_data import cus_data
# MESSAGE


from connection import databasename
import sqlite3

class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 700)
        MainWindow.setWindowIcon(QIcon('logo/logo.jpeg'))
        self.closethispage=MainWindow
        
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
        self.label_slider.setFont(QFont("sanserif",20))
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
        self.add_btn.setFont(QFont("sanserif",20))
        self.horizontalLayout_2.addWidget(self.add_btn)
        self.sale_btn = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.sale_btn.setFont(QFont("sanserif",20))
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
        self.users_btn.setFont(QFont("sanserif",20))
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
        self.customer_btn.setFont(QFont("sanserif",20))
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
        self.workers_btn.setFont(QFont("sanserif",20))
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
        self.expensive_btn.setFont(QFont("sanserif",20))
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
        self.riders_btn.setFont(QFont("sanserif",20))
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
        self.calculator_btn.setFont(QFont("sanserif",20))
        self.calculator_btn.setStyleSheet("QPushButton{\n"
"color:white;\n"
"background-color:blue;\n"
"\n"
"}")
        self.calculator_btn.setObjectName("calculator_btn")
        self.horizontalLayout_2.addWidget(self.calculator_btn)
        self.frame_3 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(30, 170, 371, 161))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(parent=self.frame_3)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(-1, 0, 361, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.lineEdit_name = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_name.setFont(font)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.horizontalLayout_3.addWidget(self.lineEdit_name)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(parent=self.frame_3)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(0, 40, 361, 41))
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
        self.lineEdit_number = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_number.setFont(font)
        self.lineEdit_number.setObjectName("lineEdit_number")
        self.horizontalLayout_4.addWidget(self.lineEdit_number)
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.frame_3)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 100, 361, 41))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.save_btn = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.save_btn.setFont(QFont("sanserif",20))
        self.save_btn.setStyleSheet("QPushButton{\n"
"background-color:blue;\n"
"color:white;\n"
"}")
        self.save_btn.setObjectName("save_btn")
        self.verticalLayout.addWidget(self.save_btn)
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
        self.lineEdit_search.setFont(QFont("sanserif",20))
        self.lineEdit_search.setObjectName("lineEdit_search")
        self.horizontalLayout_9.addWidget(self.lineEdit_search)
        self.search_btn = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_8)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.search_btn.setFont(QFont("sanserif",20))
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
        self.clear_table_btn.setFont(QFont("sanserif",20))
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
        self.create_table()
        self.save_btn.clicked.connect(self.insertdata)
        
        self.slider()
        
        self.sale_btn.clicked.connect(self.open_salespage)
        
        self.add_btn.clicked.connect(self.open_add_itempage)
        
        self.workers_btn.clicked.connect(self.open_addworkpage)
        
        self.expensive_btn.clicked.connect(self.openexpense)
        
        self.riders_btn.clicked.connect(self.openadditem)
        
        self.calculator_btn.clicked.connect(self.opencalculate)
        self.users_btn.clicked.connect(self.opencsv)
        
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Add Item Window"))
        self.label_slider.setText(_translate("MainWindow", "TextLabel"))
        self.add_btn.setText(_translate("MainWindow", "Add Item"))
        self.sale_btn.setText(_translate("MainWindow", "Sales"))
        self.users_btn.setText(_translate("MainWindow", "CSV"))
        self.customer_btn.setText(_translate("MainWindow", "Customers"))
        self.workers_btn.setText(_translate("MainWindow", "Workers"))
        self.expensive_btn.setText(_translate("MainWindow", "Expenses"))
        self.riders_btn.setText(_translate("MainWindow", "Riders"))
        self.calculator_btn.setText(_translate("MainWindow", "Calculator"))
        self.label_2.setText(_translate("MainWindow", "Name    "))
        self.label_3.setText(_translate("MainWindow", "Number"))
        self.save_btn.setText(_translate("MainWindow", "Save"))
        self.search_btn.setText(_translate("MainWindow", "Search"))
        self.clear_table_btn.setText(_translate("MainWindow", "Clear Table"))

    def create_table(self):
            self.item_table=QTableWidget(self.frame_table)
            self.item_table.setColumnCount(3)
            self.item_table.move(0,0)
            self.item_table.resize(891,361)
            self.item_table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
            self.item_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        #     self.item_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectColumns)
            self.item_table.setShowGrid(False)
            self.item_table.setWordWrap(True)
            self.item_table.setCornerButtonEnabled(False)
            self.item_table.setColumnWidth(0,100)
            self.item_table.setAlternatingRowColors(True)
            self.item_table.verticalHeader().setVisible(False)
            self.item_table.horizontalHeader().setStretchLastSection(True)
            self.item_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
            self.item_table.setSortingEnabled(True)
            self.item_table.setStyleSheet("color:black")
            self.item_table.setFont(QFont("sanserif", 10))
            self.item_table.setHorizontalHeaderLabels(['ID','Name','Number'])
        #     styling horizontalheader
            self.item_table.horizontalHeader().setStyleSheet("QHeaderView::section{background-color:black; color:white; font-size:15px}")
            self.fetch_cus()
            


    def fetch_cus(self):
           rows=cus_data()
           self.item_table.setRowCount(len(rows))
           for item,data in enumerate(rows):
                   self.item_table.setItem(item,0,QTableWidgetItem(str(data[0])))
                   self.item_table.setItem(item, 1, QTableWidgetItem(str(data[1])))
                   self.item_table.setItem(item, 2, QTableWidgetItem(str(data[2])))
                   
    def insertdata(self):
            if self.lineEdit_name.text()=="" or self.lineEdit_number.text()=="":
                    return  QMessageBox.information(self,"Information","All items must be filed")
            conn=sqlite3.connect(databasename)
            cur=conn.cursor()
            
            values=(
                    self.lineEdit_name.text(),
                    self.lineEdit_number.text()
            )
            
            cur.execute('''INSERT INTO customers (name, number) VALUES(?,?) ''', values)
            conn.commit()
            conn.close()
            self.fetch_cus()
            QMessageBox.information(self,"Information","Customer added")
            self.cleardata()

    def cleardata(self):
            self.lineEdit_name.clear()
            self.lineEdit_number.clear()
            
            
    def slider(self):
            global text,count
            Slider(self.label_slider)    
            
            
    def open_salespage(self):
            
            from sales import Ui_MainWindow
            self.salepage= QtWidgets.QMainWindow()
            self.salespage=Ui_MainWindow()
            self.salespage.setupUi(self.salepage)
            
            self.closethispage.close()
            self.salepage.show() 
            
            
    def open_add_itempage(self):
            from additemui import Ui_MainWindow
            self.addworker= QtWidgets.QMainWindow()
            self.workerpage=Ui_MainWindow()
            self.workerpage.setupUi(self.addworker)
            
            self.closethispage.close()
            self.addworker.show()
            
            
    def open_addworkpage(self):
            from workers import Ui_MainWindow
            self.addworker= QtWidgets.QMainWindow()
            self.workerpage=Ui_MainWindow()
            self.workerpage.setupUi(self.addworker)
            
            self.closethispage.close()
            self.addworker.show()
            
    def openexpense(self):
            from expenses import Ui_MainWindow
            
            self.expenses_o = QtWidgets.QMainWindow()
            self.expenses_p = Ui_MainWindow()
            self.expenses_p.setupUi(self.expenses_o)
            self.closethispage.close()
            self.expenses_o.show()



    def openadditem(self):
            from additemui import Ui_MainWindow
            
            self.addpage = QtWidgets.QMainWindow()
            self.additem = Ui_MainWindow()
            self.additem.setupUi(self.addpage)
            self.closethispage.close()
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
