#include <Python.h>

void print_python_list(PyObject *p)
{
	long int size, i;
	PyListObject *list;
	PyObject *item;

	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	list = (PyListObject *)p;
	size = Py_SIZE(p);

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);
	for (i = 0; i < size; i++)
	{
		item = PyList_GET_ITEM(p, i);
		printf("Element %ld: %s\n", i, item->ob_type->tp_name);
	}
}

void print_python_bytes(PyObject *p)
{
	long int size, i;
	PyBytesObject *bytes;
	char *str;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	bytes = (PyBytesObject *)p;
	str = bytes->ob_sval;
	size = Py_SIZE(p);

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);
	size = size + 1 > 10 ? 10 : size + 1;
	printf("  first %ld bytes: ", size);

	for (i = 0; i < size; i++)
		printf("%02hhx%s", str[i], i + 1 < size ? " " : "");
	printf("\n");
}

void print_python_float(PyObject *p)
{
	double value;

	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{			{
					printf("  [ERROR] Invalid Float Object\n");
					return;
				}
	value = ((PyFloatObject *)p)->ob_fval;
	printf("  value: %s\n", PyOS_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0, NULL));
	}
}

