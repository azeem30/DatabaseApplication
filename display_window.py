import database_home
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DISPLAY_WINDOW(object):
    def setupUi(self, DISPLAY_WINDOW):
        DISPLAY_WINDOW.setObjectName("DISPLAY_WINDOW")
        DISPLAY_WINDOW.resize(640, 480)
        DISPLAY_WINDOW.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.data_table = QtWidgets.QTableWidget(DISPLAY_WINDOW)
        self.data_table.setGeometry(QtCore.QRect(90, 50, 451, 311))
        self.data_table.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.data_table.setObjectName("data_table")
        self.data_table.setColumnCount(1)
        self.data_table.setRowCount(50)
        self.data_table.setHorizontalHeaderLabels(["NAME"])
        self.display_button = QtWidgets.QPushButton(DISPLAY_WINDOW, clicked=self.display_data)
        self.display_button.setGeometry(QtCore.QRect(260, 410, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.data_table.setFont(font)
        self.display_button.setFont(font)
        self.display_button.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.display_button.setObjectName("display_button")

        self.retranslateUi(DISPLAY_WINDOW)
        QtCore.QMetaObject.connectSlotsByName(DISPLAY_WINDOW)

    def retranslateUi(self, DISPLAY_WINDOW):
        _translate = QtCore.QCoreApplication.translate
        DISPLAY_WINDOW.setWindowTitle(_translate("DISPLAY_WINDOW", "Display"))
        self.display_button.setText(_translate("DISPLAY_WINDOW", "DISPLAY"))

    def display_data(self):
        try:
            self.cursor = database_home.data.cursor
            query = f'''SELECT * FROM {database_home.data.table_name};'''
            results = self.cursor.execute(query)
            table_row = 0
            for result in results:
                self.data_table.setItem(table_row, 0, QtWidgets.QTableWidgetItem(result[1]))
                table_row += 1
        except Exception as exception:
            database_home.ui.message_label.setText(str(exception).upper())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DISPLAY_WINDOW = QtWidgets.QWidget()
    ui = Ui_DISPLAY_WINDOW()
    ui.setupUi(DISPLAY_WINDOW)
    DISPLAY_WINDOW.show()
    sys.exit(app.exec_())
