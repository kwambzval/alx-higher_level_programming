#include <Python.h>

void print_python_list(PyObject *p)
{
	long int size = PyList_Size(p);
	int i;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < size; i++)
		printf("Element %d: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
}

void print_python_bytes(PyObject *p)
{
	char *str;
	Py_ssize_t length;
	int i;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	str = PyBytes_AS_STRING(p);
	length = PyBytes_GET_SIZE(p);
	printf("  size: %ld\n", length);
	printf("  trying string: %s\n", str);
	printf("  first %ld bytes: ", length < 10 ? length + 1 : 10);
	for (i = 0; i < length + 1 && i < 10; i++)
		printf("%02hhx%s", str[i], i + 1 < length + 1 && i + 1 < 10 ? " " : "\n");
}

