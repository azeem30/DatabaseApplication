from PyQt5 import QtCore, QtGui, QtWidgets
import insert_window, update_window, delete_window, display_window
import sqlite3

class Database:
    def __init__(self, name, table_name):
        self.name = name + ".sqlite"
        self.table_name = table_name
        self.conn = sqlite3.connect(self.name)
        self.cursor = self.conn.cursor()
        self.exception = None

    def create_table(self):
        query = f'''CREATE TABLE {self.table_name}(
                ID INT (10) PRIMARY KEY,
                NAME VARCHAR (50) NOT NULL);'''
        self.cursor.execute(query)

data = Database("test_database", "EMPLOYEE")
class Ui_window(object):
    global data
    def setupUi(self, window):
        window.setObjectName("window")
        window.resize(437, 266)
        window.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.insert = QtWidgets.QPushButton(window, clicked=self.go_insert)
        self.insert.setGeometry(QtCore.QRect(30, 130, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.insert.setFont(font)
        self.insert.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.insert.setObjectName("insert")
        self.update = QtWidgets.QPushButton(window, clicked=self.go_update)
        self.update.setGeometry(QtCore.QRect(257, 130, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.update.setFont(font)
        self.update.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.update.setObjectName("update")
        self.delete_2 = QtWidgets.QPushButton(window, clicked=self.go_delete)
        self.delete_2.setGeometry(QtCore.QRect(30, 200, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.delete_2.setFont(font)
        self.delete_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.delete_2.setObjectName("delete_2")
        self.display = QtWidgets.QPushButton(window, clicked=self.go_display)
        self.display.setGeometry(QtCore.QRect(257, 200, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.display.setFont(font)
        self.display.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.display.setObjectName("display")
        self.message_label = QtWidgets.QLabel(window)
        self.message_label.setGeometry(QtCore.QRect(30, 20, 378, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.message_label.setFont(font)
        self.message_label.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.message_label.setText("")
        self.message_label.setWordWrap(True)
        self.message_label.setObjectName("message_label")
        self.message_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.retranslateUi(window)
        QtCore.QMetaObject.connectSlotsByName(window)

    def retranslateUi(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("window", "Database Application"))
        self.insert.setText(_translate("window", "INSERT"))
        self.update.setText(_translate("window", "UPDATE"))
        self.delete_2.setText(_translate("window", "DELETE"))
        self.display.setText(_translate("window", "DISPLAY"))

    def database_related(self):
        try:
            data.create_table()
            self.message_label.setText(f"The table {data.table_name} is created successfully!")
        except Exception as exception:
            self.message_label.setText(str(exception).upper())

    def go_insert(self):
        self.ins_win = QtWidgets.QWidget()
        self.ins_ui = insert_window.Ui_INSERT_WINDOW()
        self.ins_ui.setupUi(self.ins_win)
        self.ins_win.show()

    def go_update(self):
        self.upd_win = QtWidgets.QWidget()
        self.upd_ui = update_window.Ui_UPDATE_WINDOW()
        self.upd_ui.setupUi(self.upd_win)
        self.upd_win.show()

    def go_delete(self):
        self.del_win = QtWidgets.QWidget()
        self.del_ui = delete_window.Ui_DELETE_WINDOW()
        self.del_ui.setupUi(self.del_win)
        self.del_win.show()

    def go_display(self):
        self.dis_win = QtWidgets.QWidget()
        self.dis_ui = display_window.Ui_DISPLAY_WINDOW()
        self.dis_ui.setupUi(self.dis_win)
        self.dis_win.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    ui = Ui_window()
    ui.setupUi(window)
    ui.database_related()
    window.show()
    sys.exit(app.exec_())
