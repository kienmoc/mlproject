from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements (path) -> List[str]:
    '''
        This function will return the list of requirements
    '''

    requirements = []

    with open (path, 'r') as f:
        require = f.readlines ()
        requirements = [req.replace ('\n', ' ') for req in require]
        if HYPEN_E_DOT in requirements:
            requirements.remove (HYPEN_E_DOT)
    return requirements


setup (
    name='mlproject',
    version='0.0.1',
    author='kienmoc',
    author_email='ttkien1503@gmail.com',
    packages=find_packages (),
    install_requires=get_requirements ('requirements.txt')
)