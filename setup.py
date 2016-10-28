#!/usr/bin/env python
from distutils.core import setup
    
setup(
    name = 'Messenger',
    version='0.1.0.3',
    author = "Andre Barnes",
    author_email = "abarne87@students.kennesaw.edu",
    description = ("A python Messenger"),
    packages=['Messenger'],
    platforms=["Windows", "Linux", "Solaris", "Mac OS-X", "Unix"],
    package_dir={ 'Messenger': 'Messenger'}
)
