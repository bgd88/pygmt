import numpy as np
import ctypes

data=np.ones((10,3),dtype=np.double)
out=np.empty_like(data)
#SHARED LIBRARY COMPILED WITH:
#gcc -fPIC -shared -o testlib.dylib print_array_test.c
lib = ctypes.cdll.LoadLibrary('./testlib.dylib')

analyzethis = lib.multiplyarray
print 'Input: %s' % data
analyzethis(ctypes.c_void_p(data.ctypes.data), ctypes.c_int(10), ctypes.c_int(3),ctypes.c_void_p(out.ctypes.data))
print 'Output %s' % out
#Playing with pointer
#c_float = ctypes.POINTER(ctypes.c_float)
#data = np.random.ranf((100,2)) 
#data = data.astype(np.float64)
#data_p = data.ctypes.data_as(c_float)
