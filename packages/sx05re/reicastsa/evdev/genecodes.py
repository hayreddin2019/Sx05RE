# -*- coding: utf-8; -*-

'''
Generate a Python extension module with the constants defined in linux/input.h.
'''

from __future__ import print_function
import os, sys, re


#-----------------------------------------------------------------------------
# The default header file locations to try.
headers = [
    '/usr/include/linux/input.h',
    '/usr/include/linux/input-event-codes.h',
]

if sys.argv[1:]:
    headers = sys.argv[1:]


#-----------------------------------------------------------------------------
macro_regex = r'#define +((?:KEY|ABS|REL|SW|MSC|LED|BTN|REP|SND|ID|EV|BUS|SYN|FF)_\w+)'
macro_regex = re.compile(macro_regex)

uname = list(os.uname()); del uname[1]
uname = ' '.join(uname)


#-----------------------------------------------------------------------------
template = r'''
#include <Python.h>
#ifdef __FreeBSD__
#include <dev/evdev/input.h>
#else
#include <linux/input.h>
#endif

/* Automatically generated by evdev.genecodes */
/* Generated on %s */

#define MODULE_NAME "_ecodes"
#define MODULE_HELP "linux/input.h macros"

static PyMethodDef MethodTable[] = {
    { NULL, NULL, 0, NULL}
};

#if PY_MAJOR_VERSION >= 3
static struct PyModuleDef moduledef = {
    PyModuleDef_HEAD_INIT,
    MODULE_NAME,
    MODULE_HELP,
    -1,          /* m_size */
    MethodTable, /* m_methods */
    NULL,        /* m_reload */
    NULL,        /* m_traverse */
    NULL,        /* m_clear */
    NULL,        /* m_free */
};
#endif

static PyObject *
moduleinit(void)
{

#if PY_MAJOR_VERSION >= 3
    PyObject* m = PyModule_Create(&moduledef);
#else
    PyObject* m = Py_InitModule3(MODULE_NAME, MethodTable, MODULE_HELP);
#endif

    if (m == NULL) return NULL;

%s

    return m;
}

#if PY_MAJOR_VERSION >= 3
PyMODINIT_FUNC
PyInit__ecodes(void)
{
    return moduleinit();
}
#else
PyMODINIT_FUNC
init_ecodes(void)
{
    moduleinit();
}
#endif
'''

def parse_header(header):
    for line in open(header):
        macro = macro_regex.search(line)
        if macro:
            yield '    PyModule_AddIntMacro(m, %s);' % macro.group(1)

all_macros = []
for header in headers:
    try:
        fh = open(header)
    except (IOError, OSError):
        continue
    all_macros += parse_header(header)

if not all_macros:
    print('no input macros found in: %s' % ' '.join(headers), file=sys.stderr)
    sys.exit(1)


macros = os.linesep.join(all_macros)
print(template % (uname, macros))
