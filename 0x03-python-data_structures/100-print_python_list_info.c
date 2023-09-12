#include <Python.h>
#include <object.h>
#include <listobject.h>


/**
 * print_python_list_info - prog to print a list from pyth
 * @p: file containing list to be printed
 */
void print_python_list_info(PyObject *p)
{
	long int len = PyList_Size(p);
	int count;
	PyListObject *ele_obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", len);
	printf("[*] Allocated = %li\n", ele_obj->allocated);
	for (count = 0; count < len; count++)
		printf("Element %i: %s\n", count,
				Py_TYPE(ele_obj->ob_item[count])->tp_name);
