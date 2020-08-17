#!/usr/bin/env python3


import sys

from leaden import ui


def main(argv):
    app = ui.QtWidgets.QApplication(sys.argv)
    MainWindow = ui.QtWidgets.QMainWindow()
    ui.Ui_MainWindow().setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main(argv=sys.argv[1:])
