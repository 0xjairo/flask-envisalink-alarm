import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
        name='Envisalink 3 Alarm Client',
        version='0.1',
        author='Jairo Sanchez',
        author_email='jairoscz@gmail.com',
        description='Envisalink3 client',
        license='MIT License',
        keywords='envisalink3, home alarm',
        long_description=read('README.md'),
        scripts='el3-client.py',
        )
