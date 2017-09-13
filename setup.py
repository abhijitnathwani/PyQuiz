from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst')) as f:
    long_description = f.read()

setup(
    name='py-quiz',
    version='0.1.1',
    description='Python based Quiz game.',
    long_description=long_description,
    author='Abhijit Nathwani',
    author_email='abhijit.nathwani@gmail.com',
    LICENSE='MIT',
    url='https://github.com/abhijitnathwani/PyQuiz',
    entry_points={
        'console_scripts':[
			'py-quiz = __main__:main'
			]
    },
    keywords='pyquiz tkinter'

)
