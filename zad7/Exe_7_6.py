import numpy as np
import vtk
import time


def main():

    #domek
    reader = vtk.vtkOBJReader()
    reader.SetFileName("house.obj")


    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(reader.GetOutputPort())

    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    vtkProperty = actor.GetProperty()
    vtkProperty.SetColor(0.71,0.39,0.11)
    


    #lego_man
    reader2 = vtk.vtkOBJReader()
    reader2.SetFileName("lego_man.obj")

    mapper2 = vtk.vtkPolyDataMapper()
    mapper2.SetInputConnection(reader2.GetOutputPort())

    actor2 = vtk.vtkActor()
    actor2.SetMapper(mapper2)
    vtkProperty2 = actor2.GetProperty()
    vtkProperty2.SetColor(1,1,0)
    
    vtkTransform = vtk.vtkTransform()

    vtkTransform.Scale(15,15,15)
    actor2.SetUserTransform(vtkTransform)
    actor2.SetPosition(0,0,11)

    renderer = vtk.vtkRenderer()
    rendererWindow = vtk.vtkRenderWindow()
    rendererWindow.AddRenderer(renderer)

    interactor = vtk.vtkRenderWindowInteractor()
    interactor.SetRenderWindow(rendererWindow)

    renderer.AddActor(actor)
    renderer.AddActor(actor2)

    rendererWindow.Render()


    interactor.Start()

if __name__ == "__main__":
    main()