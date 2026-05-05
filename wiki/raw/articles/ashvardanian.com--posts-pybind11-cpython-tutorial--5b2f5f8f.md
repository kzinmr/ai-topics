---
title: "Our CPython bindings got 5x faster without PyBind11 🐍"
url: "https://ashvardanian.com/posts/pybind11-cpython-tutorial/"
fetched_at: 2026-05-05T07:01:51.580949+00:00
source: "Ash Vardanyan"
tags: [blog, raw]
---

# Our CPython bindings got 5x faster without PyBind11 🐍

Source: https://ashvardanian.com/posts/pybind11-cpython-tutorial/

Python’s not the fastest language out there.
Developers often use tools like
Boost.Python
and
SWIG
to wrap faster native C/C++ code for Python.
PyBind11
is the most popular tool for the job not the quickest.
NanoBind
offers improvements, but when speed really matters, we turn to pure
CPython C API
bindings.
With
StringZilla
, I started with PyBind11 but switched to CPython to reduce latency. The switch did demand more coding effort, moving from modern C++17 to more basic C99, but the result is a 5x lower call latency! So if you want to make your bindings lighter and better understand how CPython works under the hood - continue reading 🤗
Why use CPython for StringZilla?
#
I designed StringZilla’s
Str
class to be a faster version of Python’s native
str
class. It was built for speed, handling large strings from memory-mapped files using
SIMD Assembly instructions
. Spending $50K on data-engineering tasks in public clouds this year, with StringZilla I was able to cut the processing time and costs by a factor of ten.
However, as more people suddenly started using StringZilla for smaller tasks in the last couple of months, PyBind11’s latency became noticeable:
1 microsecond using native
str
class:
"the future".find("solutions")
15 microseconds using PyBind11:
Str("the future").find("solutions")
3 microseconds using CPython:
Str("the future").find("solutions")
This is a major improvement, but you can do even better, and I’ve
already done that in SimSIMD
,
mentioned in the previous post
.
Sounds interesting? Do you want to know CPython works under the hood and how I’m leveraging that in StringZilla and my other open-source projects? Continue reading!
How is a Module Loaded?
#
Upon executing
pip install stringzilla
and subsequently running
import stringzilla
, the CPython runtime begins its search for the associated dynamic library within the directories enumerated in
sys.path
. This encompasses the current directory, any paths specified by the
PYTHONPATH
environment variable, standard library directories, and notably, the
site-packages
directory. Once CPython locates the corresponding library and verifies the presence of the initialization function,
PyInit_stringzilla
, it integrates the module within the Python environment.
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
static
PyModuleDef
stringzilla_module
=
{
PyModuleDef_HEAD_INIT
,
"stringzilla"
,
// Name
"Crunch 100+ GB Strings in Python with ease"
,
// Doc
-
1
,
// Size
stringzilla_methods
,
// A pointer to methods array
NULL
,
// An array of slot definitions for multi-phase initialization
NULL
,
// A traversal function to call during GC traversal of the module object
NULL
,
// A clear function to call during GC clearing of the module object
stringzilla_cleanup
,
// A function to call during deallocation of the module object
};
PyMODINIT_FUNC
PyInit_stringzilla
(
void
)
{
// I'm gonna use NumPy functionality from <numpy/arrayobject.h>
import_array
();
// Check our definition of the `Str` class
if
(
PyType_Ready
(
&
StrType
)
<
0
)
return
NULL
;
PyObject
*
m
=
PyModule_Create
(
&
stringzilla_module
);
if
(
m
==
NULL
)
return
NULL
;
// Add the `Str` class
Py_INCREF
(
&
StrType
);
if
(
PyModule_AddObject
(
m
,
"Str"
,
(
PyObject
*
)
&
StrType
)
<
0
)
{
Py_XDECREF
(
&
StrType
);
Py_XDECREF
(
m
);
return
NULL
;
}
// Initialize temporary_memory, if needed
temporary_memory
.
start
=
malloc
(
4096
);
temporary_memory
.
length
=
4096
*
(
temporary_memory
.
start
!=
NULL
);
return
m
;
}
Insights from the Code
:
Module Definition: Every module in Python is essentially a heap-allocated object, primarily delineated by
PyModuleDef
.
Reference Counting: Given the nature of CPython, reference management of objects is manual, necessitating the frequent utilization of functions like
Py_INCREF
and
Py_XDECREF
.
Dynamic Memory Allocation: The code introduces a static dynamically allocated
temporary_memory
. Freeing this memory is vital to avoid “memory leaks”, thus the incorporation of the
stringzilla_cleanup
function.
1
2
3
4
5
static
void
stringzilla_cleanup
(
PyObject
*
m
)
{
if
(
temporary_memory
.
start
)
free
(
temporary_memory
.
start
);
temporary_memory
.
start
=
NULL
;
temporary_memory
.
length
=
0
;
}
Module Compilation
:
Modules of this nature, rooted in C, can be compiled employing tools like CMake or Make. Alternatively, one can adapt
setup.py
to encompass this native extension.
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
setup
(
name
=
"stringzilla,
author
=
"Ash Vardanian"
,
license
=
"Apache-2.0"
,
...
include_dirs
=
[],
setup_requires
=
[
"numpy"
],
ext_modules
=
[
Extension
(
"stringzilla"
,
[
"python/lib.c"
],
include_dirs
=
[
"stringzilla"
,
numpy
.
get_include
()],
# <numpy/arrayobject.h>
extra_compile_args
=
[
"-std=c99"
,
"-O3"
,
"-pedantic"
],
# Compiler specific
extra_link_args
=
[],
define_macros
=
[],
),
],
)
Upon completion of the compilation process, the resultant artifact is a
.so
(on Linux/macOS) or
.pyd
(on Windows) shared library. A practical demonstration on macOS can be conducted by simply starting the Python runtime, and checking if the newly compiled binding can be fetched, as follows:
1
$
DYLD_PRINT_LIBRARIES
=
1
python -c
"import stringzilla"
Executing the above will display a comprehensive list, predominantly consisting of
around 80 CPython’s default dependencies
, with
stringzilla
distinctly listed therein.
How is a Function Invoked and Arguments Parsed?
#
Python’s
str
class provides a wide array of methods, offering diverse string operations. In StringZilla, apart from member methods specific to
Str
instances, I’ve also introduced global functions, enabling operations without needing an instance. These methods are enumerated in the
stringzilla_methods[]
array:
1
2
3
4
5
6
7
8
9
10
11
12
static
PyMethodDef
stringzilla_methods
[]
=
{
{
"find"
,
Str_find
,
METH_VARARGS
|
METH_KEYWORDS
,
"Find the first occurrence of a substring."
},
{
"index"
,
Str_index
,
METH_VARARGS
|
METH_KEYWORDS
,
"Find the first occurrence of a substring or raise error if missing."
},
{
"contains"
,
Str_contains
,
METH_VARARGS
|
METH_KEYWORDS
,
"Check if a string contains a substring."
},
{
"partition"
,
Str_partition
,
METH_VARARGS
|
METH_KEYWORDS
,
"Splits string into 3-tuple: before, match, after."
},
{
"count"
,
Str_count
,
METH_VARARGS
|
METH_KEYWORDS
,
"Count the occurrences of a substring."
},
{
"split"
,
Str_split
,
METH_VARARGS
|
METH_KEYWORDS
,
"Split a string by a separator."
},
{
"splitlines"
,
Str_splitlines
,
METH_VARARGS
|
METH_KEYWORDS
,
"Split a string by line breaks."
},
{
"startswith"
,
Str_startswith
,
METH_VARARGS
|
METH_KEYWORDS
,
"Check if a string starts with a given prefix."
},
{
"endswith"
,
Str_endswith
,
METH_VARARGS
|
METH_KEYWORDS
,
"Check if a string ends with a given suffix."
},
{
"levenstein"
,
Str_levenstein
,
METH_VARARGS
|
METH_KEYWORDS
,
"Calculate the Levenshtein distance between two strings."
},
{
NULL
,
NULL
,
0
,
NULL
}};
The highlighted flags combination in the snippet is
METH_VARARGS | METH_KEYWORDS
. Several flag options are available, each catering to specific requirements:
METH_VARARGS
: Standard convention, accepting a tuple with all arguments. Commonly combined with
METH_KEYWORDS
to accept keyword arguments.
METH_KEYWORDS
: For methods to receive keyword arguments, usually paired with either
METH_VARARGS
or
METH_FASTCALL
.
METH_FASTCALL
: A post-Python 3.7 optimization, this flag enhances the calling convention efficiency.
METH_NOARGS
: For methods that don’t require any arguments.
METH_O
: Suitable for methods taking just a single object argument.
METH_CLASS
and
METH_STATIC
: Specify class and static methods, respectively.
METH_COEXIST
: Permits a method’s loading even if another definition with the same name already exists.
As an illustrative example, consider the
Str_levenstein
function which calculates the Levenshtein (Edit) distance between two strings.
Depending on the way you call it,
self
, positional arguments
args
and named arguments
kwargs
will contain different values.
Method
Global Function
Member Method
Example
sz.levenstein(a, b)
a.levenstein(b)
Example with Last Positional Arg.
sz.levenstein(a, b, 10)
a.levenstein(b, 10)
Example with Last Named Arg.
sz.levenstein(a, b, bound=10)
a.levenstein(b, bound=10)
Object in
self
sz
module
a
Object in
args
a
,
b
, possibly
10
b
, possibly
10
Object in
kwargs
possibly
bound=10
possibly
bound=10
Here comes the code:
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
static
PyObject
*
Str_levenstein
(
PyObject
*
self
,
PyObject
*
args
,
PyObject
*
kwargs
)
{
// Is this a member method, or a global function? How many args is too much?
int
is_member
=
self
!=
NULL
&&
PyObject_TypeCheck
(
self
,
&
StrType
);
Py_ssize_t
nargs
=
PyTuple_Size
(
args
);
if
(
nargs
<
!
is_member
+
1
||
nargs
>
!
is_member
+
2
)
{
PyErr_Format
(
PyExc_TypeError
,
"Invalid number of arguments"
);
return
NULL
;
}
// Parse positional arguments
PyObject
*
str1_obj
=
is_member
?
self
:
PyTuple_GET_ITEM
(
args
,
0
);
PyObject
*
str2_obj
=
PyTuple_GET_ITEM
(
args
,
!
is_member
+
0
);
PyObject
*
bound_obj
=
nargs
>
!
is_member
+
1
?
PyTuple_GET_ITEM
(
args
,
!
is_member
+
1
)
:
NULL
;
if
(
kwargs
)
{
PyObject
*
key
,
*
value
;
Py_ssize_t
pos
=
0
;
while
(
PyDict_Next
(
kwargs
,
&
pos
,
&
key
,
&
value
))
if
(
PyUnicode_CompareWithASCIIString
(
key
,
"bound"
)
==
0
)
{
if
(
bound_obj
)
{
PyErr_Format
(
PyExc_TypeError
,
"Received bound both as positional and keyword argument"
);
return
NULL
;
}
bound_obj
=
value
;
}
}
int
bound
=
255
;
// Default value for bound
if
(
bound_obj
&&
((
bound
=
PyLong_AsLong
(
bound_obj
))
>
255
||
bound
<
0
))
{
PyErr_Format
(
PyExc_ValueError
,
"Bound must be an integer between 0 and 255"
);
return
NULL
;
}
sz_string_view_t
str1
,
str2
;
if
(
!
export_string_like
(
str1_obj
,
&
str1
.
start
,
&
str1
.
length
)
||
!
export_string_like
(
str2_obj
,
&
str2
.
start
,
&
str2
.
length
))
{
PyErr_Format
(
PyExc_TypeError
,
"Both arguments must be string-like"
);
return
NULL
;
}
// Allocate memory for the Levenstein matrix, or just a couple of its rows
size_t
memory_needed
=
sz_levenstein_memory_needed
(
str1
.
length
,
str2
.
length
);
if
(
temporary_memory
.
length
<
memory_needed
)
{
temporary_memory
.
start
=
realloc
(
temporary_memory
.
start
,
memory_needed
);
temporary_memory
.
length
=
memory_needed
;
}
if
(
!
temporary_memory
.
start
)
{
PyErr_Format
(
PyExc_MemoryError
,
"Unable to allocate memory for the Levenshtein matrix"
);
return
NULL
;
}
levenstein_distance_t
small_bound
=
(
levenstein_distance_t
)
bound
;
levenstein_distance_t
distance
=
sz_levenstein
(
str1
.
start
,
str1
.
length
,
str2
.
start
,
str2
.
length
,
small_bound
,
temporary_memory
.
start
);
return
PyLong_FromLong
(
distance
);
}
The function employs a substantial amount of boilerplate code:
Just 3 lines to compute and return the distance.
8 lines for temporary memory allocations and potential errors.
Over 30 lines meticulously parse the function arguments.
Most developers avoid that using the
PyArg_ParseTupleAndKeywords
function:
1
2
3
4
5
PyObject
*
str1_obj
,
*
str2_obj
,
*
bound_obj
=
NULL
;
int
bound
=
255
;
// Default value for bound
static
char
*
kwlist
[]
=
{
"str1"
,
"str2"
,
"bound"
,
NULL
};
if
(
!
PyArg_ParseTupleAndKeywords
(
args
,
kwargs
,
"OO|O"
,
kwlist
,
&
str1_obj
,
&
str2_obj
,
&
bound_obj
))
return
NULL
;
Once called,
PyArg_ParseTupleAndKeywords
in turn calls
vgetargskeywords
and creates a huge stack frame for all the temporary variables required to parse the provided arguments according to the
OO|O
format:
1
2
3
4
5
6
7
8
9
10
char
msgbuf
[
512
];
int
levels
[
32
];
const
char
*
fname
,
*
msg
,
*
custom_msg
;
int
min
=
INT_MAX
;
int
max
=
INT_MAX
;
int
i
,
pos
,
len
;
int
skip
=
0
;
Py_ssize_t
nargs
,
nkwargs
;
freelistentry_t
static_entries
[
STATIC_FREELIST_ENTRIES
];
freelist_t
freelist
;
Things go downhill from there, as 3 separate
for
-loops will have to be executed to perform the parsing.
Obviously, this is a lot more expensive then most functions inside of StringZilla, that we are going to wrap.
1
2
3
4
5
6
7
8
9
10
11
/* scan kwlist and count the number of positional-only parameters */
for
(
pos
=
0
;
kwlist
[
pos
]
&&
!*
kwlist
[
pos
];
pos
++
)
...
/* scan kwlist and get greatest possible nbr of args */
for
(
len
=
pos
;
kwlist
[
len
];
len
++
)
...
/* convert tuple args and keyword args in same loop, using kwlist to drive process */
for
(
i
=
0
;
i
<
len
;
i
++
)
...
In pursuit of further enhancements, the fast calling convention
METH_KEYWORDS | METH_FASTCALL
should be utilized, eliminating overhead associated with tuple-unpacking. If you’re interested, I’ve incorporated this approach in the recent release of
SimSIMD
. You can
reference its implementation
to grasp the improvements. Looking forward to your contributions 🤗
How is a Class Defined and Which Methods it Has?
#
Defining a Python class offers more versatility than merely specifying its methods. Let’s delve into the
Str
class in StringZilla as an illustrative example. Alongside the
PyMethodDef
methods, this class was designed to support Python’s “sequence” protocols, enabling:
Determining the string’s length:
len(Str(""))
.
Fetching a specific character:
Str("a")[0]
.
Checking substring presence:
"a" in Str("a")
.
To achieve the above, the class requires a
PySequenceMethods
definition. Furthermore, to support slicing (e.g.,
text[10:-10]
to omit the first and last 10 characters), a
PyMappingMethods
definition becomes essential.
1
2
3
4
5
6
7
8
9
10
static
PySequenceMethods
Str_as_sequence
=
{
.
sq_length
=
Str_len
,
.
sq_item
=
Str_getitem
,
.
sq_contains
=
Str_in
,
};
static
PyMappingMethods
Str_as_mapping
=
{
.
mp_length
=
Str_len
,
.
mp_subscript
=
Str_subscript
,
// Supports Python slices
};
Other notable features include:
Buffer Protocol (
Str_as_buffer
): Commonly associated with Linear Algebra and Data Science libraries, this protocol facilitates zero-copy access. It treats
Str
as a one-dimensional character array, making it reminiscent of C arrays.
1
2
3
4
static
PyBufferProcs
Str_as_buffer
=
{
.
bf_getbuffer
=
Str_getbuffer
,
.
bf_releasebuffer
=
Str_releasebuffer
,
};
Numerical Operations (
Str_as_number
): Currently, the class only supports string concatenation using the addition operator:
Str("fizz") + Str("buzz")
.
1
2
3
static
PyNumberMethods
Str_as_number
=
{
.
nb_add
=
Str_concat
,
};
These methods, combined with other essential methods like
tp_hash
for hashing (
hash(Str(""))
),
tp_richcompare
for comparisons (
< == > != <= >=
), and more, are all unified under the
StrType
structure:
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
static
PyMethodDef
Str_methods
[]
=
{
{
"find"
,
Str_find
,
METH_VARARGS
|
METH_KEYWORDS
,
"Find the first occurrence of a substring."
},
{
"index"
,
Str_index
,
METH_VARARGS
|
METH_KEYWORDS
,
"Find the first occurrence of a substring or raise error if missing."
},
{
"contains"
,
Str_contains
,
METH_VARARGS
|
METH_KEYWORDS
,
"Check if a string contains a substring."
},
{
"partition"
,
Str_partition
,
METH_VARARGS
|
METH_KEYWORDS
,
"Splits string into 3-tuple: before, match, after."
},
{
"count"
,
Str_count
,
METH_VARARGS
|
METH_KEYWORDS
,
"Count the occurrences of a substring."
},
{
"split"
,
Str_split
,
METH_VARARGS
|
METH_KEYWORDS
,
"Split a string by a separator."
},
{
"splitlines"
,
Str_splitlines
,
METH_VARARGS
|
METH_KEYWORDS
,
"Split a string by line breaks."
},
{
"startswith"
,
Str_startswith
,
METH_VARARGS
|
METH_KEYWORDS
,
"Check if a string starts with a given prefix."
},
{
"endswith"
,
Str_endswith
,
METH_VARARGS
|
METH_KEYWORDS
,
"Check if a string ends with a given suffix."
},
{
"levenstein"
,
Str_levenstein
,
METH_VARARGS
|
METH_KEYWORDS
,
"Calculate the Levenshtein distance between two strings."
},
{
NULL
,
NULL
,
0
,
NULL
}};
static
PyTypeObject
StrType
=
{
PyObject_HEAD_INIT
(
NULL
).
tp_name
=
"stringzilla.Str"
,
.
tp_doc
=
"Immutable string/slice class with SIMD and SWAR-accelerated operations"
,
.
tp_basicsize
=
sizeof
(
Str
),
.
tp_flags
=
Py_TPFLAGS_DEFAULT
,
.
tp_new
=
Str_new
,
.
tp_init
=
Str_init
,
.
tp_dealloc
=
Str_dealloc
,
.
tp_hash
=
Str_hash
,
.
tp_richcompare
=
Str_richcompare
,
.
tp_str
=
Str_str
,
.
tp_methods
=
Str_methods
,
.
tp_as_sequence
=
&
Str_as_sequence
,
.
tp_as_mapping
=
&
Str_as_mapping
,
.
tp_as_buffer
=
&
Str_as_buffer
,
.
tp_as_number
=
&
Str_as_number
,
};
Our Accomplishments
#
I put StringZilla to the test using the well-known Leipzig 1M dataset, which is 129,644,797 bytes in size. A standout feature of StringZilla is its ability to avoid unnecessary data copies. This is particularly beneficial when using functions like
partition
and
split
on large datasets, as it leads to significant memory savings. Moreover, the
File
class empowers us to handle datasets that exceed available memory.
Here’s a comparative performance chart:
Task
Python
StringZilla
Speed Boost
.count("the")
150 ms
50 ms
3x
.count("\n")
49 ms
11 ms
4.5x
.split("the")
223 ms
57 ms
3.9x
.split("\n")
100 ms
34 ms
2.9x
.partition("the")
8 ms
259 ns
31x
.partition("\n")
8 ms
264 ns
31x
.find("\n")
247 ns
172 ns
1.4x
¹
.find("wzyx")
70 ms
8 ms
8.8x
¹ The accuracy of this value might be off. In reality, StringZilla could be slightly slower. The challenge lies in measuring such short durations, especially using tools like the Jupyter notebook I employed.
Lately, I’ve been primarily leveraging low-level direct CPython bindings in projects such as:
SimSIMD
– For computations that outpace SciPy and NumPy in vector similarity.
UCall
– A turbocharged alternative to FastAPI.
I’m also contemplating their integration in
USearch
which we use to replace FAISS, and
UForm
, to serve faster multi-modal inference API.
Looking forward to your contributions, and don’t forget to share with your friends, if the projects resonate 🤗
