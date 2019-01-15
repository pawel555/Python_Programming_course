import sys
import vtk

from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5 import Qt
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor


def cmd_exit():
    app.quit()


class ImportButton(QWidget):
    def __init__(self, lay, lst, parent=None):
        QWidget.__init__(self, parent)
        self.btn = QPushButton('Select files to load:')
        self.btn.clicked.connect(self.upload_files)
        self.lst = lst
        lay.addWidget(self.btn, 0, 0, 1, 2)

    def upload_files(self):
        names = QFileDialog.getOpenFileNames(self, 'Open file')
        for name in names[0]:
            self.lst.addItem(name)


class DeleteButton(QWidget):
    def __init__(self, lay, lst, parent=None):
        QWidget.__init__(self, parent)
        self.lst = lst
        self.btn = QPushButton('Delete selected')
        self.btn.clicked.connect(self.delete_selected)
        lay.addWidget(self.btn, 1, 5, 1, 2)

    def delete_selected(self):
        item = self.lst.currentRow()
        print(item)
        self.lst.takeItem(item)


class STLList(QWidget):
    def __init__(self, lay, parent=None):
        QWidget.__init__(self, parent)
        self.lst = QListWidget()
        lay.addWidget(self.lst, 1, 0, 1, 5)
        self.iren = None
        self.lst.itemClicked.connect(self.set_stl)
        self.vtkWidget = None

    def set_stl(self):
        # filename = "files/Part_1.stl"
        filename = str(self.lst.currentItem().text())
        print(filename)

        reader = vtk.vtkSTLReader()
        reader.SetFileName(filename)

        mapper = vtk.vtkPolyDataMapper()
        if vtk.VTK_MAJOR_VERSION <= 5:
            mapper.SetInput(reader.GetOutput())
        else:
            mapper.SetInputConnection(reader.GetOutputPort())

        actor = vtk.vtkActor()
        actor.SetMapper(mapper)

        self.vtkWidget = QVTKRenderWindowInteractor()

        ren = vtk.vtkRenderer()
        self.vtkWidget.GetRenderWindow().AddRenderer(ren)
        self.iren = self.vtkWidget.GetRenderWindow().GetInteractor()

        ren.AddActor(actor)
        ren.ResetCamera()

        lay.addWidget(self.vtkWidget, 3, 0, 1, 6)

        self.iren_refresh()


    def iren_refresh(self):
        self.iren.Initialize()
        self.iren.Start()

    def get_list(self):
        return self.lst

    def get_vtk_widget(self):
        return self.vtkWidget


app = QApplication(sys.argv)

lay = QGridLayout()

lbl2 = QLabel("wpisz sciezke pliku")

lay.addWidget(lbl2, 0, 2, 1, 5)

stl_lst = STLList(lay)

lbl = ImportButton(lay, stl_lst.get_list())

dlt = DeleteButton(lay, stl_lst.get_list())

lbl3 = QLabel('VTK Preview of selected items:')
lay.addWidget(lbl3, 2, 0, 1, 6)

btn2 = QPushButton('Quit')
btn2.clicked.connect(cmd_exit)
lay.addWidget(btn2, 4, 0, 1, 1)

w = QWidget()
w.setFixedWidth(800)
w.setFixedHeight(1100)
w.move(100, 100)
w.setLayout(lay)
w.show()

# stl_lst.iren_refresh()

app.exec_()
