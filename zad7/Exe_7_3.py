import vtk


def main():
    cubeSource = vtk.vtkCubeSource()
    cubeSource.SetCenter (0,0,0)
    cubeSource.SetXLength (2.5)
    cubeSource.SetYLength (3.5)
    cubeSource.SetZLength (4.5)
    
    # Create a mapper and actor
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(cubeSource.GetOutputPort())
    #1
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(255, 0, 0)
    #2
    cubeSource2 = vtk.vtkCubeSource()
    cubeSource2.SetCenter (0,10,0)
    cubeSource2.SetXLength (2.5)
    cubeSource2.SetYLength (3.5)
    cubeSource2.SetZLength (4.5)
    mapper2 = vtk.vtkPolyDataMapper()
    mapper2.SetInputConnection(cubeSource2.GetOutputPort())
    actor2 = vtk.vtkActor()
    actor2.SetMapper(mapper2)
    actor2.GetProperty().SetColor(0, 255, 0)

    #3
    cubeSource3 = vtk.vtkCubeSource()
    cubeSource3.SetCenter (10,0,0)
    cubeSource3.SetXLength (2.5)
    cubeSource3.SetYLength (3.5)
    cubeSource3.SetZLength (4.5)
    mapper3 = vtk.vtkPolyDataMapper()
    mapper3.SetInputConnection(cubeSource3.GetOutputPort())
    actor3 = vtk.vtkActor()
    actor3.SetMapper(mapper3)
    actor3.GetProperty().SetColor(0, 0, 255)

    #4
    cubeSource4 = vtk.vtkCubeSource()
    cubeSource4.SetCenter (10,10,0)
    cubeSource4.SetXLength (2.5)
    cubeSource4.SetYLength (3.5)
    cubeSource4.SetZLength (4.5)
    mapper4 = vtk.vtkPolyDataMapper()
    mapper4.SetInputConnection(cubeSource4.GetOutputPort())
    actor4 = vtk.vtkActor()
    actor4.SetMapper(mapper4)
    actor4.GetProperty().SetColor(255, 255, 0)

    #lightwhite
    lightWhite = vtk.vtkLight()
    lightWhite.SetPosition(100.0, 100.0, 0.0)
    lightWhite.SetColor(1.0, 1.0, 1.0)
    lightWhite.SetIntensity(0.2)

    #lightred
    lightRed = vtk.vtkLight()
    lightRed.SetColor(1.0, 0.0, 0.0)
    lightRed.SetPosition(-100, 0.0, 0.0)
    lightRed.SetIntensity(0.7)

    #lightblue
    lightBlue = vtk.vtkLight()
    lightBlue.SetColor(0.0, 0.0, 1.0)
    lightBlue.SetPosition(100.0, 0.0, 10.0)
    lightBlue.SetIntensity(0.3)

    # Visualize
    renderer = vtk.vtkRenderer()
    renderWindow = vtk.vtkRenderWindow()
    renderWindow.AddRenderer(renderer)
    renderWindowInteractor = vtk.vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)
    renderer.AddActor(actor)
    renderer.AddActor(actor2)
    renderer.AddActor(actor3)
    renderer.AddActor(actor4)

    renderer.AddLight(lightWhite)
    renderer.AddLight(lightRed)
    renderer.AddLight(lightBlue)
    renderer.SetBackground(1,1,1)
    renderWindow.Render()
    renderWindowInteractor.Start()


if __name__ == "__main__":
    main()