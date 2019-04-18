from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import os

a = os.listdir()
all_file = []

ext_modules = []

for i in a:
    if i.endswith('.py'):
        all_file.append(i)
for i in all_file:
    

    ext_modules.append(Extension(i[0:-3], [i]))
setup(
    name = 'My Program',
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules
)
