#include <listobject.h>
#include <object.h>

/**
 * print_python_list_info - function that prints some basic info about Python lists
 * @p: python list
 */
void print_python_list_info(PyObject *p)
{
	PyObject *obj;
	int size, alloc, x;
	
	alloc = ((PyListobject *)p)->allocated;
	size = Py_SIZE(p);

	printf("[*] Size of the Python list = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);
	
	for (x = 0; x < size; x++)
	{
		printf("Element %d:", x);
		obj = Py_List_Getitem(p, x)
			printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
