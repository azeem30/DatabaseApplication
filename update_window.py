from PyQt5 import QtCore, QtGui, QtWidgets
import database_home

class Ui_UPDATE_WINDOW(object):
    def setupUi(self, UPDATE_WINDOW):
        UPDATE_WINDOW.setObjectName("UPDATE_WINDOW")
        UPDATE_WINDOW.resize(391, 215)
        UPDATE_WINDOW.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label = QtWidgets.QLabel(UPDATE_WINDOW)
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
        self.label_2 = QtWidgets.QLabel(UPDATE_WINDOW)
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
        self.id_updated = QtWidgets.QLineEdit(UPDATE_WINDOW)
        self.id_updated.setGeometry(QtCore.QRect(110, 47, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.id_updated.setFont(font)
        self.id_updated.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);d")
        self.id_updated.setText("")
        self.id_updated.setObjectName("id_updated")
        self.name_updated = QtWidgets.QLineEdit(UPDATE_WINDOW)
        self.name_updated.setGeometry(QtCore.QRect(133, 77, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.name_updated.setFont(font)
        self.name_updated.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);d")
        self.name_updated.setText("")
        self.name_updated.setObjectName("name_updated")
        self.update_button = QtWidgets.QPushButton(UPDATE_WINDOW, clicked=self.update_data)
        self.update_button.setGeometry(QtCore.QRect(290, 180, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.update_button.setFont(font)
        self.update_button.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.update_button.setObjectName("update_button")
        self.update_message = QtWidgets.QLabel(UPDATE_WINDOW)
        self.update_message.setGeometry(QtCore.QRect(50, 120, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.update_message.setFont(font)
        self.update_message.setStyleSheet("color: rgb(255, 255, 255);")
        self.update_message.setText("")
        self.update_message.setWordWrap(True)
        self.update_message.setObjectName("update_message")

        self.retranslateUi(UPDATE_WINDOW)
        QtCore.QMetaObject.connectSlotsByName(UPDATE_WINDOW)

    def retranslateUi(self, UPDATE_WINDOW):
        _translate = QtCore.QCoreApplication.translate
        UPDATE_WINDOW.setWindowTitle(_translate("UPDATE_WINDOW", "Update"))
        self.label.setText(_translate("UPDATE_WINDOW", "ID"))
        self.label_2.setText(_translate("UPDATE_WINDOW", "Name"))
        self.update_button.setText(_translate("UPDATE_WINDOW", "UPDATE"))

    def update_data(self):
        try:
            self.cursor = database_home.data.cursor
            updated_ID = int(self.id_updated.text())
            updated_name = self.name_updated.text()
            query = f'''UPDATE EMPLOYEE SET NAME = '{updated_name}' WHERE ID = {updated_ID};'''
            self.cursor.execute(query)
            database_home.data.conn.commit()
            self.update_message.setText(f"Record Updated Successfully in {database_home.data.table_name}!")
        except Exception as exception:
            self.update_message.setText(str(exception).upper())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UPDATE_WINDOW = QtWidgets.QWidget()
    ui = Ui_UPDATE_WINDOW()
    ui.setupUi(UPDATE_WINDOW)
    UPDATE_WINDOW.show()
    sys.exit(app.exec_())
