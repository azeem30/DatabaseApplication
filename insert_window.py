from PyQt5 import QtCore, QtGui, QtWidgets
import database_home

class Ui_INSERT_WINDOW(object):
    def setupUi(self, INSERT_WINDOW):
        INSERT_WINDOW.setObjectName("INSERT_WINDOW")
        INSERT_WINDOW.resize(391, 215)
        INSERT_WINDOW.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label = QtWidgets.QLabel(INSERT_WINDOW)
        self.label.setGeometry(QtCore.QRect(80, 50, 21, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(INSERT_WINDOW)
        self.label_2.setGeometry(QtCore.QRect(80, 80, 51, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.id_entry = QtWidgets.QLineEdit(INSERT_WINDOW)
        self.id_entry.setGeometry(QtCore.QRect(110, 47, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.id_entry.setFont(font)
        self.id_entry.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);d")
        self.id_entry.setText("")
        self.id_entry.setObjectName("id_entry")
        self.name_entry = QtWidgets.QLineEdit(INSERT_WINDOW)
        self.name_entry.setGeometry(QtCore.QRect(133, 77, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.name_entry.setFont(font)
        self.name_entry.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);d")
        self.name_entry.setText("")
        self.name_entry.setObjectName("name_entry")
        self.add_button = QtWidgets.QPushButton(INSERT_WINDOW, clicked=self.add_data)
        self.add_button.setGeometry(QtCore.QRect(290, 180, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.add_button.setFont(font)
        self.add_button.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.add_button.setObjectName("add_button")
        self.insert_message = QtWidgets.QLabel(INSERT_WINDOW)
        self.insert_message.setGeometry(QtCore.QRect(50, 120, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.insert_message.setFont(font)
        self.insert_message.setStyleSheet("color: rgb(255, 255, 255);")
        self.insert_message.setText("")
        self.insert_message.setWordWrap(True)
        self.insert_message.setObjectName("insert_message")

        self.retranslateUi(INSERT_WINDOW)
        QtCore.QMetaObject.connectSlotsByName(INSERT_WINDOW)

    def retranslateUi(self, INSERT_WINDOW):
        _translate = QtCore.QCoreApplication.translate
        INSERT_WINDOW.setWindowTitle(_translate("INSERT_WINDOW", "Insert"))
        self.label.setText(_translate("INSERT_WINDOW", "ID"))
        self.label_2.setText(_translate("INSERT_WINDOW", "Name"))
        self.add_button.setText(_translate("INSERT_WINDOW", "ADD"))

    def add_data(self):
        try:
            self.cursor = database_home.data.cursor
            entered_ID = self.id_entry.text()
            int_ID = int(entered_ID)
            entered_name = self.name_entry.text()
            query = f'''INSERT INTO EMPLOYEE(ID, NAME) VALUES({int_ID}, '{entered_name}');'''
            self.cursor.execute(query)
            database_home.data.conn.commit()
            self.insert_message.setText("Record inserted successfully!")
        except Exception as exception:
            self.insert_message.setText(str(exception).upper())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    INSERT_WINDOW = QtWidgets.QWidget()
    ui = Ui_INSERT_WINDOW()
    ui.setupUi(INSERT_WINDOW)
    INSERT_WINDOW.show()
    sys.exit(app.exec_())
