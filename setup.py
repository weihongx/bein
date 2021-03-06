from distutils.core import setup
setup(name='bein',
      version='1.06',
      url='http://madhadron.com/bein',
      description='Miniature LIMS and workflow manager for bioinformatics',
      author='Fred Ross',
      author_email='madhadron@gmail.com',
      packages=['bein'],
      scripts=['add_nh_flag'],
      classifiers=['Topic :: System :: Shells', 'Topic :: Scientific/Engineering :: Bio-Informatics'],
      install_requires = ['unittest2'],
      )
