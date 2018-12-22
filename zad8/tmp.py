import sys
from PyQt5.QtWidgets import *


def cmd_exit():
    app.quit()

app = QApplication(sys.argv)

lay = QHBoxLayout()

lbl = QLabel("Select file to show:")
lay.addWidget(lbl)

btn = QPushButton("Save As")
lay.addWidget(btn)

btn2 = QPushButton("Quit")
btn2.clicked.connect(cmd_exit)
lay.addWidget(btn2)

lay.addStretch()

w = QWidget()
w.move(0, 0)
w.setLayout(lay)
w.show()

app.exec_()
