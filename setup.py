# You have to write below codes in setup.py

from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:  # gives o/p as list of str 
    '''This function returns a list of requirements'''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines() # when it read next line '\n' get stored in list so remove that
        requirements = [req.replace("\n","") for req in requirements] 

    if '-e .' in requirements:
        requirements.remove('-e .')

    return requirements

# setup function in setup.py to install project in pip
setup(
    name="MLProjects",
    version="0.0.1", # version of pypi where ML projects are installed and we can also upload this project there
    author='Rakeshhh',
    author_email='swainrakesh35@gmail.com',
    packages=find_packages(),
    # install_requires=['pandas','numpy','seaborn'],
    install_requires=get_requirements('requirements.txt'), # go to requirements.txt and install all required packages
)