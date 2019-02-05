from setuptools import setup

setup(name='dsqss',
      version='2.0.0',
      description='DSQSS input files generator',
      url='https://github.com/issp-center-dev/dsqss',
      author='DSQSS developers',
      author_email='dsqss-dev@issp.u-tokyo.ac.jp',
      packages=['dsqss'],
      python_requires='>=2.7',
      install_requires=['numpy', 'toml'],
      entry_points={
          'console_scripts':[
              'dla_hamgen = dsqss.hamgen:main',
              'dla_latgen = dsqss.latgen:main',
              'dla_alg = dsqss.dla_alg:main',
              'dla_pre = dsqss.dla_pre:main',
              ]
          },
      zip_safe=False,
      )