#!/usr/bin/env python
"""Catalysis Micro-kinetic Analysis Package (CatMAP)"""

import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
#from catmap import __version__ as version
__version__ = "0.3.1"

maintainer = 'Andrew J. Medford'
maintainer_email = 'ajmedfor@slac.stanford.edu'
author = maintainer
author_email = maintainer_email
description =  __doc__
classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: X11 Applications :: GTK',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Operating System :: POSIX :: Windows',
        'Programming Language :: Fortran',
        'Programming Language :: Python',
        'Topic :: Education',
        'Topic :: Scientific/Engineering :: Chemistry',
        'Topic :: Scientific/Engineering :: Physics',
        'Topic :: Scientific/Engineering :: Visualization',
              ]
requires = ['ase',
            'matplotlib',
            'mpmath',
            'numpy',
            'graphviz'
                   ]
license = 'COPYING.txt'
long_description = open('README.md').read()
name='python-catmap'
packages = [
           'catmap',
           'catmap.analyze',
           'catmap.api',
           'catmap.data',
           'catmap.mappers',
           'catmap.parsers',
           'catmap.scalers',
           'catmap.solvers',
           'catmap.thermodynamics',
           ]
package_dir = {'catmap':'catmap'}
package_data = {'catmap':[]}
platforms = ['linux', 'windows']
if os.name == 'nt':__version__ = "0.3.1"
    scripts = []
else:
    scripts = [
        'tools/catmap'
              ]

url = 'https://github.com/ajmedford/catmap'

setup(
      author=author,
      author_email=author_email,
      description=description,
      license=license,
      long_description=long_description,
      maintainer=maintainer,
      maintainer_email=maintainer_email,
      name=name,
      package_data=package_data,
      package_dir=package_dir,
      packages=packages,
      platforms=platforms,
      scripts=scripts,
      url=url,
      version=version,
      install_requires = ['ase>=3.17',
            'matplotlib',
            'mpmath',
            'numpy',
            'graphviz']
      )
