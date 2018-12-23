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
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    # Visualize
    renderer = vtk.vtkRenderer()
    renderWindow = vtk.vtkRenderWindow()
    renderWindow.AddRenderer(renderer)
    renderWindowInteractor = vtk.vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)
    renderer.AddActor(actor)
    renderWindow.Render()
    renderWindowInteractor.Start()


if __name__ == "__main__":
    main()