from distutils.core import setup
from Cython.Build import cythonize
from distutils.extension  import Extension

setup(name='speedup',
      ext_modules=cythonize([Extension("speedup"["speedup.py"])])