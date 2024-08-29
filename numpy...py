Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import numpy as np
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import numpy as np
ModuleNotFoundError: No module named 'numpy'

================================ RESTART: Shell ================================
import numpy as np
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    import numpy as np
ModuleNotFoundError: No module named 'numpy'

================================ RESTART: Shell ================================
import numpy as np
a=np.array([5,6,9])
a[0]
np.int64(5)
a[2]
np.int64(9)
a=np.array([[1,2],[3])
           
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
a=np.array([[1,2],[3,4]])
           
a=np.array([[1,2],[3,4],[5,6]])
           
a.ndim
           
2
 a,itemsize
           
SyntaxError: unexpected indent
a.itemsize
           
8
a.dtype
           
dtype('int64')
a=np.array([[1,2],[3,4],[5,6]], dtype=np.float64)
           
a.itemsize
           
8
a
           
array([[1., 2.],
       [3., 4.],
       [5., 6.]])














a.sixe
           
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    a.sixe
AttributeError: 'numpy.ndarray' object has no attribute 'sixe'. Did you mean: 'size'?
a.sixe
           
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    a.sixe
AttributeError: 'numpy.ndarray' object has no attribute 'sixe'. Did you mean: 'size'?
a.size
           
6
a
           
array([[1., 2.],
       [3., 4.],
       [5., 6.]])
a.shape
           
(3, 2)
a=np.array([[1,2],[3,4],[5,6]], dtype=complex)
           
a
           
array([[1.+0.j, 2.+0.j],
       [3.+0.j, 4.+0.j],
       [5.+0.j, 6.+0.j]])




import numpy as np
np.zeros ((3,4))
array([[0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.]])
np.ones((3,4))
array([[1., 1., 1., 1.],
       [1., 1., 1., 1.],
       [1., 1., 1., 1.]])
1=range
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
1=range(5)
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
l=range(5)
l
range(0, 5)
l[0]
0
l[2]
2
no.arang(1,5)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    no.arang(1,5)
NameError: name 'no' is not defined. Did you mean: 'np'?
np.arang(1,5)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    np.arang(1,5)
  File "C:\Users\yeamu\AppData\Roaming\Python\Python312\site-packages\numpy\__init__.py", line 428, in __getattr__
    raise AttributeError("module {!r} has no attribute "
AttributeError: module 'numpy' has no attribute 'arang'. Did you mean: 'arange'?
np.arange(1,5)
                         
array([1, 2, 3, 4])
array([1, 2, 3, 4])
                         
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    array([1, 2, 3, 4])
NameError: name 'array' is not defined. Did you forget to import 'array'?
np.arange(1,5,2)
                         
array([1, 3])
np.linspace(1,5,10)
                         
array([1.        , 1.44444444, 1.88888889, 2.33333333, 2.77777778,
       3.22222222, 3.66666667, 4.11111111, 4.55555556, 5.        ])
np.linspace(1,5,20)
                         
array([1.        , 1.21052632, 1.42105263, 1.63157895, 1.84210526,
       2.05263158, 2.26315789, 2.47368421, 2.68421053, 2.89473684,
       3.10526316, 3.31578947, 3.52631579, 3.73684211, 3.94736842,
       4.15789474, 4.36842105, 4.57894737, 4.78947368, 5.        ])
4.15789474, 4.36842105, 4.57894737, 4.78947368, 5.        ])
SyntaxError: unmatched ']'







import numpy as np
a=np.array([[1,2],[3,4],[5,6]])
a
array([[1, 2],
       [3, 4],
       [5, 6]])
a.shape
(3, 2)
a.reshape(2,3)
array([[1, 2, 3],
       [4, 5, 6]])
a.reshape(2,1)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    a.reshape(2,1)
ValueError: cannot reshape array of size 6 into shape (2,1)
a.reshape(6,1)
array([[1],
       [2],
       [3],
       [4],
       [5],
       [6]])
a.ravel()
array([1, 2, 3, 4, 5, 6])
a
array([[1, 2],
       [3, 4],
       [5, 6]])

a.main()
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    a.main()
AttributeError: 'numpy.ndarray' object has no attribute 'main'. Did you mean: 'min'?
ammax()
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    ammax()
NameError: name 'ammax' is not defined
a.max()
np.int64(6)
a.min()
np.int64(1)
a.sum()
np.int64(21)
a.sum(axis=0)
array([ 9, 12])
a.sum(axis=1)
array([ 3,  7, 11])



np.sqrt(a)
array([[1.        , 1.41421356],
       [1.73205081, 2.        ],
       [2.23606798, 2.44948974]])
>>> a
array([[1, 2],
       [3, 4],
       [5, 6]])
>>> np.std.(a)
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> import numpy as np
>>> a= np.array([[1,2],[3,4]])
>>> b= np.array([[5,6],[7,8]])
>>> a
array([[1, 2],
       [3, 4]])
>>> b
array([[5, 6],
       [7, 8]])
>>> a+b
array([[ 6,  8],
       [10, 12]])
>>> a/b
array([[0.2       , 0.33333333],
       [0.42857143, 0.5       ]])
>>> a*b
array([[ 5, 12],
       [21, 32]])
>>> a/b
array([[0.2       , 0.33333333],
       [0.42857143, 0.5       ]])
>>> a.dot(b)
array([[19, 22],
       [43, 50]])
