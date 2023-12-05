#include <object.h>
#include <python.h>
/**
 * print_python_list_info - function that prints some basic info about Python lists
 * @p: python list
 */
void print_python_list_info(PyObject *p)
{
	long int size = PyList_Size(p);
	int x;
	PyListobject *oo = (PyListobject *)p;

	printf("[*] Size of the Python list = %li\n", size);
	printf("[*] Allocated = %li\n", oo->Allocated);
	for (x = 0; x < size; x++)
		printf("Element %i: %s\n", i, Py_TYPE(oo->ob_item[x]->type_name);
}
