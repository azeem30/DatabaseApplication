from PyQt5 import QtCore, QtGui, QtWidgets
import database_home

class Ui_DELETE_WINDOW(object):
    def setupUi(self, DELETE_WINDOW):
        DELETE_WINDOW.setObjectName("DELETE_WINDOW")
        DELETE_WINDOW.resize(391, 215)
        DELETE_WINDOW.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label = QtWidgets.QLabel(DELETE_WINDOW)
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
        self.id_deleted = QtWidgets.QLineEdit(DELETE_WINDOW)
        self.id_deleted.setGeometry(QtCore.QRect(110, 47, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(10)
        self.id_deleted.setFont(font)
        self.id_deleted.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);d")
        self.id_deleted.setText("")
        self.id_deleted.setObjectName("id_deleted")
        self.deleted_button = QtWidgets.QPushButton(DELETE_WINDOW, clicked=self.delete_data)
        self.deleted_button.setGeometry(QtCore.QRect(290, 180, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.deleted_button.setFont(font)
        self.deleted_button.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.deleted_button.setObjectName("deleted_button")
        self.delete_message = QtWidgets.QLabel(DELETE_WINDOW)
        self.delete_message.setGeometry(QtCore.QRect(50, 100, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.delete_message.setFont(font)
        self.delete_message.setStyleSheet("color: rgb(255, 255, 255);")
        self.delete_message.setText("")
        self.delete_message.setWordWrap(True)
        self.delete_message.setObjectName("delete_message")

        self.retranslateUi(DELETE_WINDOW)
        QtCore.QMetaObject.connectSlotsByName(DELETE_WINDOW)

    def retranslateUi(self, DELETE_WINDOW):
        _translate = QtCore.QCoreApplication.translate
        DELETE_WINDOW.setWindowTitle(_translate("DELETE_WINDOW", "Delete"))
        self.label.setText(_translate("DELETE_WINDOW", "ID"))
        self.deleted_button.setText(_translate("DELETE_WINDOW", "DELETE"))

    def delete_data(self):
        try:
            self.cursor = database_home.data.cursor
            deleted_ID = int(self.id_deleted.text())
            query = f'''DELETE FROM EMPLOYEE WHERE ID = {deleted_ID};'''
            self.cursor.execute(query)
            database_home.data.conn.commit()
            self.delete_message.setText(f"Record Deleted Successfully from {database_home.data.table_name}!")
        except Exception as exception:
            self.delete_message.setText(str(exception).upper())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DELETE_WINDOW = QtWidgets.QWidget()
    ui = Ui_DELETE_WINDOW()
    ui.setupUi(DELETE_WINDOW)
    DELETE_WINDOW.show()
    sys.exit(app.exec_())
