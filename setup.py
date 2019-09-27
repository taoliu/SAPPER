#!/usr/bin/env python
# Time-stamp: <2019-09-27 16:44:56 taoliu>

"""Description: 

Setup script for SAPPER

This code is free software; you can redistribute it and/or modify it
under the terms of the BSD License (see the file LICENSE included with
the distribution).
"""

import os
import sys
from setuptools import setup, Extension

# Use build_ext from Cython if found
command_classes = {}
try:
    import Cython.Distutils
    command_classes['build_ext'] = Cython.Distutils.build_ext
    from Cython.Build import cythonize
    has_cython = True
except:
    has_cython = False

try: 
    from numpy import get_include as numpy_get_include 
    numpy_include_dir = [numpy_get_include()] 
except: 
    numpy_include_dir = []
    
def main():
    if float(sys.version[:3])<3.6:
        sys.stderr.write("CRITICAL: Python version must be larger than 3.6!\n")
        sys.exit(1)

    # I intend to use -Ofast, however if gcc version < 4.6, this option is unavailable so...
    extra_c_args = ["-w","-O3","-ffast-math"] # for C, -Ofast implies -O3 and -ffast-math

    if has_cython:
        ext_modules = [Extension("SAPPER.PeakIO",["SAPPER/PeakIO.pyx",],libraries=["m"], include_dirs=numpy_include_dir, extra_compile_args=extra_c_args),
                       Extension("SAPPER.ReadAlignment",["SAPPER/ReadAlignment.pyx",],libraries=["m"],include_dirs=numpy_include_dir, extra_compile_args=extra_c_args),
                       Extension("SAPPER.RACollection",["SAPPER/RACollection.pyx","fermi-lite/bfc.c","fermi-lite/bseq.c","fermi-lite/bubble.c","fermi-lite/htab.c","fermi-lite/ksw.c","fermi-lite/kthread.c","fermi-lite/mag.c","fermi-lite/misc.c","fermi-lite/mrope.c","fermi-lite/rld0.c","fermi-lite/rle.c","fermi-lite/rope.c","fermi-lite/unitig.c", "SAPPER/swalign.c"],libraries=["m","z"], include_dirs=numpy_include_dir+["./","./fermi-lite/","./SAPPER/"], extra_compile_args=extra_c_args),
                       Extension("SAPPER.UnitigRACollection",["SAPPER/UnitigRACollection.pyx"],libraries=["m"], include_dirs=numpy_include_dir, extra_compile_args=extra_c_args),
                       Extension("SAPPER.PosReadsInfo",["SAPPER/PosReadsInfo.pyx",],libraries=["m"], include_dirs=numpy_include_dir, extra_compile_args=extra_c_args),
                       Extension("SAPPER.PeakVariants",["SAPPER/PeakVariants.pyx",],libraries=["m"], include_dirs=numpy_include_dir, extra_compile_args=extra_c_args),                 
                       Extension("SAPPER.Stat",["SAPPER/Stat.pyx",],libraries=["m"], include_dirs=numpy_include_dir, extra_compile_args=extra_c_args),
                       Extension("SAPPER.Prob",["SAPPER/Prob.pyx",],libraries=["m"], include_dirs=numpy_include_dir, extra_compile_args=extra_c_args),
                       Extension("SAPPER.BAM",["SAPPER/BAM.pyx",],libraries=["m"], include_dirs=numpy_include_dir, extra_compile_args=extra_c_args)]
        ext_modules = cythonize(ext_modules, language_level=3)
    else:
        ext_modules = [Extension("SAPPER.PeakIO",["SAPPER/PeakIO.c",],libraries=["m"], include_dirs=numpy_include_dir, extra_compile_args=extra_c_args),
                       Extension("SAPPER.ReadAlignment",["SAPPER/ReadAlignment.c",],libraries=["m"],include_dirs=numpy_include_dir, extra_compile_args=extra_c_args),
                       Extension("SAPPER.RACollection",["SAPPER/RACollection.c","fermi-lite/bfc.c","fermi-lite/bseq.c","fermi-lite/bubble.c","fermi-lite/htab.c","fermi-lite/ksw.c","fermi-lite/kthread.c","fermi-lite/mag.c","fermi-lite/misc.c","fermi-lite/mrope.c","fermi-lite/rld0.c","fermi-lite/rle.c","fermi-lite/rope.c","fermi-lite/unitig.c", "SAPPER/swalign.c"],libraries=["m","z"], include_dirs=numpy_include_dir+["./","./fermi-lite/","./SAPPER/"], extra_compile_args=extra_c_args),
                       Extension("SAPPER.UnitigRACollection",["SAPPER/UnitigRACollection.c"],libraries=["m"], include_dirs=numpy_include_dir, extra_compile_args=extra_c_args),
                       Extension("SAPPER.PosReadsInfo",["SAPPER/PosReadsInfo.c",],libraries=["m"], include_dirs=numpy_include_dir, extra_compile_args=extra_c_args),
                       Extension("SAPPER.PeakVariants",["SAPPER/PeakVariants.c",],libraries=["m"], include_dirs=numpy_include_dir, extra_compile_args=extra_c_args),                 
                       Extension("SAPPER.Stat",["SAPPER/Stat.c",],libraries=["m"], include_dirs=numpy_include_dir, extra_compile_args=extra_c_args),
                       Extension("SAPPER.Prob",["SAPPER/Prob.c",],libraries=["m"], include_dirs=numpy_include_dir, extra_compile_args=extra_c_args),
                       Extension("SAPPER.BAM",["SAPPER/BAM.c",],libraries=["m"], include_dirs=numpy_include_dir, extra_compile_args=extra_c_args)]

    setup(name="SAPPER",
          version="1.0.2",
          description="de novo variant caller for DNA enrichment assays",
          author='Tao Liu',
          author_email='vladimir.liu@gmail.com',
          url='http://github.com/taoliu/SAPPER/',
          package_dir={'SAPPER' : 'SAPPER'},
          packages=['SAPPER',],
          scripts=['bin/sapper'],
          classifiers=[
              'Development Status :: 4 - Beta',
              'Environment :: Console',
              'Intended Audience :: Developers',
              'Intended Audience :: Science/Research',              
              'License :: OSI Approved :: BSD License',
              'Operating System :: MacOS :: MacOS X',
              'Operating System :: POSIX',
              'Topic :: Scientific/Engineering :: Bio-Informatics',
              'Programming Language :: Python',
              ],
          install_requires=[
              'numpy>=1.15'
              ],
          cmdclass = command_classes,
          ext_modules = ext_modules,
          )

if __name__ == '__main__':
    main()
