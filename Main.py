#!/usr/bin/env python3
# coding=utf-8

import sys
from random import randint

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('uis/main.ui', self)  # загрузка формы в py-скрипт
        self.setWindowTitle('Работа с визуальными табличными данными в Python')
        self.setWindowIcon(QtGui.QIcon('images/logo.png'))
        self.btn_random_number.clicked.connect(self.fill_random_numbers)
        self.btn_solve.clicked.connect(self.solve)

    def fill_random_numbers(self):
        """
        заполняем таблицу случайными числами
        :return:
        """
        row = 0
        col = 0
        # заполняем таблицу случайными числами
        while row < self.tableWidget.rowCount():
            while col < self.tableWidget.columnCount():
                random_num = randint(0, 100)
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(random_num)))
                col += 1
            row += 1
            col = 0
        self.label_error.setText('')
        self.label_max_el.setText('Нажмите кнопку "Выполнить задание"')

    def solve(self):
        if find_zero(self.tableWidget) == 1:
            row = 0
            col = 0
            while row < self.tableWidget.rowCount():
                while col < self.tableWidget.columnCount():
                    self.tableWidget.setItem(row, col, QTableWidgetItem('1'))
                    col += 1
                row += 1
                col = 0
            self.label_max_el.setText('Задание выполнено')
        else:
            self.label_max_el.setText('Нет нулевого элемента')


def find_zero(table_widget):
    zero_count = 0;
    try:
        row = 0
        col = 0
        while row < table_widget.rowCount():
            while col < table_widget.columnCount():
                number = float(table_widget.item(row, col).text())
                if number == 0:
                    zero_count += 1
                col += 1
            row += 1
            col = 0
        if zero_count > 0:
            return 1
    except Exception:
        return 0


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
