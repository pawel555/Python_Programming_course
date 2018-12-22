import sys
import PyQt5

from PyQt5.QtWidgets import *

file_shown = ''

# 4278519045
def cmd_exit():
    app.quit()


def convert_image():
    img = pic_lbl.pixmap().toImage()
    for x in range(0, img.width()):
        for y in range(0, img.height()):
            # red = PyQt5.QtGui.qGray(img.pixel(x, y))
            red = PyQt5.QtGui.qRed(img.pixel(x, y))
            green = PyQt5.QtGui.qGreen(img.pixel(x, y))
            blue = PyQt5.QtGui.qBlue(img.pixel(x, y))
            color = (red * int(txt1.text()) + green * int(txt2.text()) + blue * int(txt3.text())) / 32
            img.setPixel(x, y, PyQt5.QtGui.QColor(color, color, color).rgb())
    print('Done')

    pxmp = PyQt5.QtGui.QPixmap.fromImage(img)
    pic_lbl.setPixmap(pxmp)


class SaveButton(QWidget):
    def __init__(self, lay, parent=None):
        QWidget.__init__(self, parent)
        self.btn = QPushButton('Save As')
        self.btn.clicked.connect(self.save_image)
        lay.addWidget(self.btn, 10, 0, 1, 1)

    def save_image(self):
        name = QFileDialog.getSaveFileName(self, 'Save file')
        p = pic_lbl.pixmap()
        p.save(name[0])


class ImportButton(QWidget):
    def __init__(self, lay, parent=None):
        QWidget.__init__(self, parent)
        self.btn = QPushButton('Select file to show:')
        self.btn.clicked.connect(self.upload_image)
        lay.addWidget(self.btn, 0, 0, 1, 2)

    def upload_image(self):
        name = QFileDialog.getOpenFileName(self, 'Open file')
        pic_lbl.setPixmap(PyQt5.QtGui.QPixmap(name[0]))
        global file_shown
        file_shown = name[0]


app = QApplication(sys.argv)

lay = QGridLayout()

lbl = ImportButton(lay)

lbl2 = QLabel("no file chosen")
# lbl2 = QFileDialog()
lay.addWidget(lbl2, 0, 2, 1, 4)

lbl3 = QLabel('ICON')
lay.addWidget(lbl3, 0, 6, 1, 1)

plhldr = QLabel('')
lay.addWidget(plhldr, 1, 1, 1, 6 )

lbl4 = QLabel('Convert to grayscale')
lay.addWidget(lbl4, 2, 0, 1, 2)

lbl5 = QLabel('Red weight:')
lay.addWidget(lbl5, 3, 0, 1, 1)

txt1 = QLineEdit('11')
txt1.setFixedWidth(40)
lay.addWidget(txt1, 3, 1, 1, 1)

lbl6 = QLabel('Blue weight:')
lay.addWidget(lbl6, 3, 2, 1, 1)

txt2 = QLineEdit('16')
txt2.setFixedWidth(40)
lay.addWidget(txt2, 3, 3, 1, 1)

lbl7 = QLabel('Red weight:')
lay.addWidget(lbl7, 3, 4, 1, 1)

txt3 = QLineEdit('5')
txt3.setFixedWidth(40)
lay.addWidget(txt3, 3, 5, 1, 1)

cnv = QPushButton('Convert')
cnv.clicked.connect(convert_image)
lay.addWidget(cnv, 3, 6, 1, 1)

lbl8 = QLabel('Formula: (r*c.red() + b*c.blue() + g*c.green())/32')
lay.addWidget(lbl8, 4, 0, 1, 6)

lbl9 = QLabel('(Assume the colors are in range 0-255.)')
lay.addWidget(lbl9, 5, 0, 1, 6)

pic_lbl = QLabel()
pic_lbl.setFixedWidth(700)
pic_lbl.setFixedHeight(700)
lay.addWidget(pic_lbl, 7, 0, 1, 6)

btn = SaveButton(lay)

btn2 = QPushButton('Quit')
btn2.clicked.connect(cmd_exit)
lay.addWidget(btn2, 10, 1, 1, 1)

w = QWidget()
w.setFixedWidth(800)
w.setFixedHeight(1100)
w.move(100, 100)
w.setLayout(lay)
w.show()

app.exec_()
