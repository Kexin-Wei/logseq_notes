- `vtkNew` and `vtkSmartPointer`
  collapsed:: true
	- Both `vtkNew` and `vtkSmartPointer` are used for managing the memory of VTK objects. The key difference between them lies in their intended use cases and how they manage memory allocation and deallocation.
	- vtkNew:
	  `vtkNew` is a lightweight smart pointer specifically designed for stack-allocated VTK objects. When you create a VTK object using `vtkNew`, the memory is automatically allocated and deallocated when the `vtkNew` object goes out of scope. `vtkNew` is more efficient and straightforward to use for local variables in a function or method. However, it does not support transferring ownership or changing the underlying VTK object.
	  
	  Example of using `vtkNew`:
	  ```cpp
	  #include <vtkNew.h>
	  #include <vtkPolyData.h>
	  
	  void MyFunction() {
	    vtkNew<vtkPolyData> polyData;
	  
	    // Use polyData in your function
	    // ...
	  }
	  ```
	- vtkSmartPointer:
	  `vtkSmartPointer` is a more flexible smart pointer that allows for reference counting and shared ownership of VTK objects. It can be used with both stack and heap-allocated VTK objects. When the last `vtkSmartPointer` referencing an object goes out of scope or is reassigned, the VTK object's memory is automatically deallocated. `vtkSmartPointer` is better suited for situations where ownership of VTK objects needs to be shared or transferred between different parts of your program, or when working with heap-allocated objects.
	  
	  Example of using `vtkSmartPointer`:
	  ```cpp
	  #include <vtkSmartPointer.h>
	  #include <vtkPolyData.h>
	  
	  vtkSmartPointer<vtkPolyData> MyFunction() {
	    vtkSmartPointer<vtkPolyData> polyData = vtkSmartPointer<vtkPolyData>::New();
	  
	    // Use polyData in your function
	    // ...
	  
	    return polyData;
	  }
	  ```
	  
	  In summary, when deciding which one to use in a function, consider the following:
	- If you are working with a local VTK object that will not be shared or transferred outside the function, use `vtkNew` for efficiency and simplicity.
	- If you need to share or transfer the ownership of a VTK object between different parts of your program, or you are working with heap-allocated objects, use `vtkSmartPointer`.
	- Using the appropriate smart pointer for your use case ensures better memory management and can prevent memory leaks or other issues related to manual memory management.
- 3D Surface Extractor
	- [vtkFlyingEdges3D](https://vtk.org/doc/nightly/html/classvtkFlyingEdges3D.html)
	- [vtkMarchingCubes](https://vtk.org/doc/nightly/html/classvtkMarchingCubes.html)
	- [vtkContour3DLinearGrid](https://vtk.org/doc/nightly/html/classvtkContour3DLinearGrid.html)
- 2D Contour Extract from Mesh / Polydata
	- `vtkCutter`+`vtkKochanekSpline`+`vtkSplineFilter`
- BSpline Mesh Library
	- [Rhino - The openNURBS initiative (rhino3d.com)](https://www.rhino3d.com/it/features/developer/opennurbs/)
	- [SINTEF-Geometry/SISL: The SINTEF Spline Library (github.com)](https://github.com/SINTEF-Geometry/SISL)