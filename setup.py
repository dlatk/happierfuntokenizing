from setuptools import setup

DESCRIPTION = """This code implements a basic, Twitter-aware tokenizer. Originally developed by Christopher Potts and 
updated by the World Well-Being Project based out of the University of Pennsylvania and Stony Brook University. Shared with permission."""

DISTNAME = 'happierfuntokenizing'
LICENSE = 'GNU General Public License v3 (GPLv3)'
AUTHOR = "Christopher Potts, H. Andrew Schwartz, Maarten Sap, Salvatore Giorgi"
EMAIL = "hansens@sas.upenn.edu, sgiorgi@sas.upenn.edu"
MAINTAINER = "Salvatore Giorgi, H. Andrew Schwartz"
MAINTAINER_EMAIL = "sgiorgi@sas.upenn.edu, hansens@sas.upenn.edu"
URL = 'http://dlatk.wwbp.org'
DOWNLOAD_URL = 'https://github.com/dlatk/happierfuntokenizing'
CLASSIFIERS = [
  'Environment :: Console',
  'Natural Language :: English',
  'Intended Audience :: End Users/Desktop',
  'Intended Audience :: Developers',
  'Intended Audience :: Science/Research',
  'Programming Language :: Python :: 3',
  'Programming Language :: Python :: 3.5',
  'Programming Language :: Python :: 3.6',
  'Programming Language :: Python :: 3.7',
  'Programming Language :: Python :: 3.8',
  'Programming Language :: Python :: 3.9',
  'Topic :: Scientific/Engineering',
]
VERSION = '1.1'

if __name__ == "__main__":

  setup(name=DISTNAME,
      author=AUTHOR,
      author_email=EMAIL, 
      version=VERSION,
      description=DESCRIPTION,
      license=LICENSE,
      url=URL,
      download_url=DOWNLOAD_URL,
      classifiers=CLASSIFIERS,
  )
