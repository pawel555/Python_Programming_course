import sys

from PyQt5.QtWidgets import *


def cmd_exit():
    app.quit()


class ImportButton(QWidget):
    def __init__(self, lay, parent=None):
        QWidget.__init__(self, parent)
        self.btn = QPushButton('Select files to load:')
        self.btn.clicked.connect(self.upload_files)
        lay.addWidget(self.btn, 0, 0, 1, 2)

    def upload_files(self):
        names = QFileDialog.getOpenFileNames(self, 'Open file')
        for name in names[0]:
            lst.addItem(name)


class DeleteButton(QWidget):
    def __init__(self, lay, parent=None):
        QWidget.__init__(self, parent)
        self.btn = QPushButton('Delete selected')
        self.btn.clicked.connect(self.delete_selected)
        lay.addWidget(self.btn, 1, 5, 1, 2)

    def delete_selected(self):
        item = lst.currentRow()
        print(item)
        lst.takeItem(item)


app = QApplication(sys.argv)

lay = QGridLayout()

lbl = ImportButton(lay)

lbl2 = QLabel("wpisz sciezke pliku")

lay.addWidget(lbl2, 0, 2, 1, 5)

lst = QListWidget()
lay.addWidget(lst, 1, 0, 1, 5)

dlt = DeleteButton(lay)

lbl3 = QLabel('VTK Preview of selected items:')
lay.addWidget(lbl3, 2, 0, 1, 6)

pic_lbl = QLabel()
pic_lbl.setFixedWidth(700)
pic_lbl.setFixedHeight(700)
lay.addWidget(pic_lbl, 3, 0, 1, 6)

btn2 = QPushButton('Quit')
btn2.clicked.connect(cmd_exit)
lay.addWidget(btn2, 4, 0, 1, 1)

w = QWidget()
w.setFixedWidth(800)
w.setFixedHeight(1100)
w.move(100, 100)
w.setLayout(lay)
w.show()

app.exec_()
