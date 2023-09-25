import sys
#sys.path.append(r"c:\Users\cuddly\ABC\1")

#from ui_serialPort import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets, QtSerialPort
#以下本来是ui_serialPort.py里的内容。
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(410, 343)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_rece = QtWidgets.QLabel(self.centralwidget)
        self.label_rece.setObjectName("label_rece")
        self.verticalLayout_3.addWidget(self.label_rece)
        self.textEdit_rece = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_rece.setObjectName("textEdit_rece")
        self.verticalLayout_3.addWidget(self.textEdit_rece)
        self.label_send = QtWidgets.QLabel(self.centralwidget)
        self.label_send.setObjectName("label_send")
        self.verticalLayout_3.addWidget(self.label_send)
        self.textEdit_send = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_send.setObjectName("textEdit_send")
        self.verticalLayout_3.addWidget(self.textEdit_send)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_clear = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.horizontalLayout_6.addWidget(self.pushButton_clear)
        self.pushButton_send = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_send.setObjectName("pushButton_send")
        self.horizontalLayout_6.addWidget(self.pushButton_send)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_port = QtWidgets.QLabel(self.centralwidget)
        self.label_port.setObjectName("label_port")
        self.horizontalLayout.addWidget(self.label_port)
        self.comboBox_port = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_port.setObjectName("comboBox_port")
        self.horizontalLayout.addWidget(self.comboBox_port)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_baud = QtWidgets.QLabel(self.centralwidget)
        self.label_baud.setObjectName("label_baud")
        self.horizontalLayout_2.addWidget(self.label_baud)
        self.comboBox_baud = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_baud.setObjectName("comboBox_baud")
        self.comboBox_baud.addItem("")
        self.comboBox_baud.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_baud)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_data = QtWidgets.QLabel(self.centralwidget)
        self.label_data.setObjectName("label_data")
        self.horizontalLayout_3.addWidget(self.label_data)
        self.comboBox_data = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_data.setObjectName("comboBox_data")
        self.comboBox_data.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox_data)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_test = QtWidgets.QLabel(self.centralwidget)
        self.label_test.setObjectName("label_test")
        self.horizontalLayout_4.addWidget(self.label_test)
        self.comboBox_test = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_test.setObjectName("comboBox_test")
        self.comboBox_test.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox_test)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_stop = QtWidgets.QLabel(self.centralwidget)
        self.label_stop.setObjectName("label_stop")
        self.horizontalLayout_5.addWidget(self.label_stop)
        self.comboBox_stop = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_stop.setObjectName("comboBox_stop")
        self.comboBox_stop.addItem("")
        self.horizontalLayout_5.addWidget(self.comboBox_stop)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.pushButton_search = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_search.setObjectName("pushButton_search")
        self.verticalLayout_2.addWidget(self.pushButton_search)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.pushButton_serial = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_serial.setObjectName("pushButton_serial")
        self.verticalLayout_2.addWidget(self.pushButton_serial)
        self.horizontalLayout_7.addLayout(self.verticalLayout_2)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_7)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_rece.setText(_translate("MainWindow", "接受窗口"))
        self.label_send.setText(_translate("MainWindow", "发送窗口"))
        self.pushButton_clear.setText(_translate("MainWindow", "清空接受"))
        self.pushButton_send.setText(_translate("MainWindow", "发送数据"))
        self.label_port.setText(_translate("MainWindow", "串口号:"))
        self.label_baud.setText(_translate("MainWindow", "波特率:"))
        self.comboBox_baud.setItemText(0, _translate("MainWindow", "9600"))
        self.comboBox_baud.setItemText(1, _translate("MainWindow", "115200"))
        self.label_data.setText(_translate("MainWindow", "数据位："))
        self.comboBox_data.setItemText(0, _translate("MainWindow", "8"))
        self.label_test.setText(_translate("MainWindow", "校验位："))
        self.comboBox_test.setItemText(0, _translate("MainWindow", "0"))
        self.label_stop.setText(_translate("MainWindow", "停止位："))
        self.comboBox_stop.setItemText(0, _translate("MainWindow", "1"))
        self.pushButton_search.setText(_translate("MainWindow", "检测串口"))
        self.pushButton_serial.setText(_translate("MainWindow", "打开串口"))



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(410, 343)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_rece = QtWidgets.QLabel(self.centralwidget)
        self.label_rece.setObjectName("label_rece")
        self.verticalLayout_3.addWidget(self.label_rece)
        self.textEdit_rece = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_rece.setObjectName("textEdit_rece")
        self.verticalLayout_3.addWidget(self.textEdit_rece)
        self.label_send = QtWidgets.QLabel(self.centralwidget)
        self.label_send.setObjectName("label_send")
        self.verticalLayout_3.addWidget(self.label_send)
        self.textEdit_send = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_send.setObjectName("textEdit_send")
        self.verticalLayout_3.addWidget(self.textEdit_send)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_clear = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.horizontalLayout_6.addWidget(self.pushButton_clear)
        self.pushButton_send = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_send.setObjectName("pushButton_send")
        self.horizontalLayout_6.addWidget(self.pushButton_send)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_port = QtWidgets.QLabel(self.centralwidget)
        self.label_port.setObjectName("label_port")
        self.horizontalLayout.addWidget(self.label_port)
        self.comboBox_port = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_port.setObjectName("comboBox_port")
        self.horizontalLayout.addWidget(self.comboBox_port)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_baud = QtWidgets.QLabel(self.centralwidget)
        self.label_baud.setObjectName("label_baud")
        self.horizontalLayout_2.addWidget(self.label_baud)
        self.comboBox_baud = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_baud.setObjectName("comboBox_baud")
        self.comboBox_baud.addItem("")
        self.comboBox_baud.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_baud)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_data = QtWidgets.QLabel(self.centralwidget)
        self.label_data.setObjectName("label_data")
        self.horizontalLayout_3.addWidget(self.label_data)
        self.comboBox_data = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_data.setObjectName("comboBox_data")
        self.comboBox_data.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox_data)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_test = QtWidgets.QLabel(self.centralwidget)
        self.label_test.setObjectName("label_test")
        self.horizontalLayout_4.addWidget(self.label_test)
        self.comboBox_test = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_test.setObjectName("comboBox_test")
        self.comboBox_test.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox_test)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_stop = QtWidgets.QLabel(self.centralwidget)
        self.label_stop.setObjectName("label_stop")
        self.horizontalLayout_5.addWidget(self.label_stop)
        self.comboBox_stop = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_stop.setObjectName("comboBox_stop")
        self.comboBox_stop.addItem("")
        self.horizontalLayout_5.addWidget(self.comboBox_stop)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.pushButton_search = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_search.setObjectName("pushButton_search")
        self.verticalLayout_2.addWidget(self.pushButton_search)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.pushButton_serial = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_serial.setObjectName("pushButton_serial")
        self.verticalLayout_2.addWidget(self.pushButton_serial)
        self.horizontalLayout_7.addLayout(self.verticalLayout_2)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_7)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_rece.setText(_translate("MainWindow", "接受窗口"))
        self.label_send.setText(_translate("MainWindow", "发送窗口"))
        self.pushButton_clear.setText(_translate("MainWindow", "清空接受"))
        self.pushButton_send.setText(_translate("MainWindow", "发送数据"))
        self.label_port.setText(_translate("MainWindow", "串口号:"))
        self.label_baud.setText(_translate("MainWindow", "波特率:"))
        self.comboBox_baud.setItemText(0, _translate("MainWindow", "9600"))
        self.comboBox_baud.setItemText(1, _translate("MainWindow", "115200"))
        self.label_data.setText(_translate("MainWindow", "数据位："))
        self.comboBox_data.setItemText(0, _translate("MainWindow", "8"))
        self.label_test.setText(_translate("MainWindow", "校验位："))
        self.comboBox_test.setItemText(0, _translate("MainWindow", "0"))
        self.label_stop.setText(_translate("MainWindow", "停止位："))
        self.comboBox_stop.setItemText(0, _translate("MainWindow", "1"))
        self.pushButton_search.setText(_translate("MainWindow", "检测串口"))
        self.pushButton_serial.setText(_translate("MainWindow", "打开串口"))


#以上本来是ui_serialPort.py里的内容。

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.serial = QtSerialPort.QSerialPort(self)
        self.ui.pushButton_send.setEnabled(False)
        self.ui.comboBox_baud.setCurrentIndex(1)

        self.slot_init()

    def slot_init(self):
        self.ui.pushButton_serial.clicked.connect(self.pushButton_serial_clicked)
        self.ui.pushButton_search.clicked.connect(self.pushButton_search_clicked)
        self.ui.pushButton_send.clicked.connect(self.pushButton_send_clicked)
        self.ui.pushButton_clear.clicked.connect(self.pushButton_clear_clicked)
        self.serial.readyRead.connect(self.serialPort_readyRead)

    def serialPort_readyRead(self):
        buffer = self.serial.read(1)
        print(buffer)

        buffer = str(buffer, encoding='utf-8')
        recStr = self.ui.textEdit_rece.toPlainText()
        recStr += buffer
        self.ui.textEdit_rece.clear()
        self.ui.textEdit_rece.append(recStr)

    def pushButton_send_clicked(self):
        data = bytes(self.ui.textEdit_send.toPlainText(), encoding='utf-8')
        data = QtCore.QByteArray(data)
        self.serial.write(data)

    def pushButton_clear_clicked(self):
        self.ui.textEdit_rece.clear()

    def pushButton_search_clicked(self):
        self.ui.comboBox_port.clear()

        for i in QtSerialPort.QSerialPortInfo.availablePorts():  # 静态函数
            self.ui.comboBox_port.addItem(i.portName())

    def pushButton_serial_clicked(self):
        if self.ui.pushButton_serial.text() == str("打开串口"):
            self.serial.setPortName(self.ui.comboBox_port.currentText())
            self.serial.setBaudRate(QtSerialPort.QSerialPort.Baud115200)
            self.serial.setDataBits(QtSerialPort.QSerialPort.Data8)
            self.serial.setParity(QtSerialPort.QSerialPort.NoParity)
            self.serial.setStopBits(QtSerialPort.QSerialPort.OneStop)
            self.serial.setFlowControl(QtSerialPort.QSerialPort.NoFlowControl)

            self.ui.pushButton_serial.setText("关闭串口")
            if not self.serial.open(QtCore.QIODevice.ReadWrite):
                QtWidgets.QMessageBox.about(self,"提示","无法打开串口!")
                return

            self.ui.comboBox_baud.setEnabled(False)
            self.ui.comboBox_data.setEnabled(False)
            self.ui.comboBox_port.setEnabled(False)
            self.ui.comboBox_stop.setEnabled(False)
            self.ui.comboBox_test.setEnabled(False)

            self.ui.pushButton_send.setEnabled(True)
        elif self.ui.pushButton_serial.text() == str("关闭串口"):
            self.serial.close()
            self.ui.pushButton_serial.setText("打开串口")

            self.ui.comboBox_baud.setEnabled(True)
            self.ui.comboBox_data.setEnabled(True)
            self.ui.comboBox_port.setEnabled(True)
            self.ui.comboBox_stop.setEnabled(True)
            self.ui.comboBox_test.setEnabled(True)

            self.ui.pushButton_send.setEnabled(False)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())

"""
这是一个简单的Python程序，使用了PyQt5库来创建一个串口工具。程序主要包含以下功能：

1.打开/关闭串口
2.搜索可用串口
3.设置串口参数（波特率、数据位、校验位、停止位、流量控制）
4.发送数据
5.接收数据
6.清空接收缓冲区
7.程序使用了UI文件（ui_serialPort.ui）来设置串口工具的界面。在UI文件中，我们可以看到许多控件，如组合框（comboBox）、文本框（textEdit）、按钮（pushButton）等。这些控件在代码中对应的一个个槽函数进行连接，以便在用户点击相应控件时执行相应的操作。

在MainWindow类中，我们定义了一些槽函数，如slot_init用于初始化槽函数，pushButton_send_clicked用于发送数据，pushButton_clear_clicked用于清空接收缓冲区等。在这些槽函数中，我们使用了QtSerialPort库来处理串口相关操作。

最后，在if __name__ == "__main__":部分，我们创建了一个QApplication对象，并创建了一个MainWindow对象。然后，我们显示这个窗口，并运行QApplication的事件循环。当程序退出时，QApplication对象会自动退出。
"""


